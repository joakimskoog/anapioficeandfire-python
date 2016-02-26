import ujson as json


class BaseModel(object):

    def __init__(self, api_data):
        json_data = json.loads(api_data)

        for key, value in json_data:
            setattr(self, key, value)


class Book(BaseModel):

    def __init__(self, api_data):
        super(Book, self).__init__(api_data)


    def get_characters(self):
        return None


    def get_pov_characters(self):
        return None


class Character(BaseModel):

    def __init__(self, api_data):
        super(Character, self).__init__(api_data)


    def get_allegiances(self):
        return None


    def get_books(self):
        return None


    def get_pov_books(self):
        return None


class House(BaseModel):

    def __init__(self, api_data):
        super(House, self).__init__(api_data)


    def get_current_lord(self):
        return None


    def get_heir(self):
        return None


    def get_overlord(self):
        return None


    def get_founder(self):
        return None


    def get_cadet_branches(self):
        return None


    def get_sworn_members(self):
        return None



