# -*- coding: utf-8 -*-

try:
    from anapioficeandfire.cursor import Cursor
except:
    from cursor import Cursor

class Model(object):

    def __init__(self, api=None):
        self.api = api

    @classmethod
    def parse(cls, api, json_data):
        raise NotImplementedError()

    @classmethod
    def parse_list(cls, api, json_data):
        results = []

        for data in json_data:
            if data:
                results.append(cls.parse(api, data))
        return results

    @classmethod
    def retrieve_id(cls, url):
        index_of_last_slash = url.rindex('/')
        id = url[index_of_last_slash+1:]

        return id

    @classmethod
    def retrieve_ids(cls, urls):
        return list(map(cls.retrieve_id, urls))


class Book(Model):

    @classmethod
    def parse(cls, api, json_data):
        book = cls(api)
        for key, value in json_data.items():
            setattr(book, key, value)

        return book

    def get_characters(self):
        ids = Model.retrieve_ids(self.characters)
        cursor = Cursor(self.api.get_character, ids=ids)

        return cursor

    def get_pov_characters(self):
        ids = Model.retrieve_ids(self.povCharacters)
        cursor = Cursor(self.api.get_character, ids=ids)

        return cursor

class Character(Model):

    @classmethod
    def parse(cls, api, json_data):
        character = cls(api)
        for key, value in json_data.items():
            setattr(character, key, value)

        return character

    def get_allegiances(self):
        ids = Model.retrieve_ids(self.allegiances)
        cursor = Cursor(self.api.get_house, ids=ids)

        return cursor

    def get_books(self):
        ids = Model.retrieve_ids(self.books)
        cursor = Cursor(self.api.get_book, ids=ids)

        return cursor

    def get_pov_books(self):
        ids = Model.retrieve_ids(self.povBooks)
        cursor = Cursor(self.api.get_book, ids=ids)

        return cursor


class House(Model):

    @classmethod
    def parse(cls, api, json_data):
        house = cls(api)
        for key, value in json_data.items():
            setattr(house, key, value)

        return house

    def get_current_lord(self):
        id = Model.retrieve_id(self.currentLord)
        return self.api.get_character(id=id)

    def get_heir(self):
        id = Model.retrieve_id(self.heir)
        return self.api.get_character(id=id)

    def get_overlord(self):
        id = Model.retrieve_id(self.overlord)
        return self.api.get_house(id=id)

    def get_founder(self):
        id = Model.retrieve_id(self.founder)
        return self.api.get_character(id=id)

    def get_cadet_branches(self):
        ids = Model.retrieve_ids(self.cadetBranches)
        cursor = Cursor(self.api.get_house, ids=ids)

        return cursor

    def get_sworn_members(self):
        ids = Model.retrieve_ids(self.swornMembers)
        cursor = Cursor(self.api.get_character, ids=ids)

        return cursor


class ModelFactory(object):
    book = Book
    character = Character
    house = House

    def create(self, model_type):
        return getattr(self, model_type)

