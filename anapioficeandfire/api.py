# -*- coding: utf-8 -*-

try:
    from anapioficeandfire.binder import bind_api
    from anapioficeandfire.parsers import ModelParser
    from anapioficeandfire.models import ModelFactory
except:
    from binder import bind_api
    from parsers import ModelParser
    from models import ModelFactory


class API(object):

    def __init__(self,
                 host='anapioficeandfire.com/api',
                 api_version = 1,
                 parser = None,
                 model_factory = None):

        """ Api instance Constructor

        :param host: url of the server of the rest api, default: 'anapioficeandfire.com/api'
        :param api_version: version of the api, default: 1
        """

        self.host = host
        self.api_version = api_version
        self.parser = parser or ModelParser(model_factory or ModelFactory())

    @property
    def get_books(self):
        """ Return pages with books that matches the given parameters

        :return:
        """
        return bind_api(api=self,
                        path = '/books',
                        model_type='book',
                        allowed_parameters=['page', 'name', 'from_release_date', 'to_release_date'],
                        is_data_list=True,
                        iteration_mode='page')

    @property
    def get_book(self):
        """ Return a single book

        :param id: the id of the book
        :return: Book object
        """
        return bind_api(api = self,
                        path = '/books/{id}',
                        model_type = 'book',
                        allowed_parameters=['id'],
                        iteration_mode='id')

    @property
    def get_characters(self):
        """ Return pages with characters that matches the given parameters

        :return:
        """
        return bind_api(api=self,
                        path='/characters',
                        model_type='character',
                        allowed_parameters=['page', 'name', 'culture', 'born', 'died', 'is_alive'],
                        is_data_list=True,
                        iteration_mode='page')

    @property
    def get_character(self):
        """ Return a single character

        :param id: the id of the character
        :return: Character object
        """
        return bind_api(api=self,
                        path='/characters/{id}',
                        model_type='character',
                        allowed_parameters=['id'],
                        iteration_mode='id')

    @property
    def get_houses(self):
        """ Return pages with houses that matches the given parameters

        :return:
        """
        return bind_api(api=self,
                        path='/houses',
                        model_type='house',
                        allowed_parameters=['page', 'name', 'region', 'words', 'has_words', 'has_titles', 'has_seats', 'has_died_out', 'has_ancestral_weapons'],
                        is_data_list=True,
                        iteration_mode='page')

    @property
    def get_house(self):
        """ Return a single house

        :param id: the id of the house
        :return: House object
        """
        return bind_api(api=self,
                        path='/houses/{id}',
                        model_type='house',
                        allowed_parameters=['id'],
                        iteration_mode='id')

