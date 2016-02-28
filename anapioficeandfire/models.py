try:
    from anapioficeandfire.utils import query
    import ujson as json
except:
    import settings
    from utils import query
    import ujson as json


class ModelCursor(object):

    def __init__(self, urls, model):
        self.urls = urls
        self.total_number_of_urls = len(urls)
        self.model = model

    def __iter__(self):
        self.current_index = 0
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self.current_index == self.total_number_of_urls:
            raise StopIteration

        data = query(self.urls[self.current_index])

        if len(data.content) == 0:
            raise StopIteration

        self.current_index += 1
        return self.model(data.content)


class BaseModel(object):

    def __init__(self, api_data):
        json_data = json.loads(api_data)

        for key, value in json_data.items():
            setattr(self, key, value)


class Book(BaseModel):

    def __init__(self, api_data):
        super(Book, self).__init__(api_data)

    def get_characters(self):
        return ModelCursor(self.characters, Character)

    def get_pov_characters(self):
        return ModelCursor(self.povCharacters, Character)


class Character(BaseModel):

    def __init__(self, api_data):
        super(Character, self).__init__(api_data)

    def get_allegiances(self):
        return ModelCursor(self.allegiances, House)

    def get_books(self):
        return ModelCursor(self.books, Book)

    def get_pov_books(self):
        return ModelCursor(self.povBooks, Book)


class House(BaseModel):

    def __init__(self, api_data):
        super(House, self).__init__(api_data)

    def get_current_lord(self):
        response = query(self.currentLord)
        return Character(response.content)

    def get_heir(self):
        response = query(self.heir)
        return Character(response.content)

    def get_overlord(self):
        response = query(self.overlord)
        return House(response.content)

    def get_founder(self):
        response = query(self.founder)
        return Character(response.content)

    def get_cadet_branches(self):
        return ModelCursor(self.cadetBranches, House)

    def get_sworn_members(self):
        return ModelCursor(self.swornMembers, Character)



