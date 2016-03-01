
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
    def get_book(self):
        """ Return a single book

        :param id: the id of the book
        :return: Book object
        """
        return bind_api(api = self,
                        path = '/books/{id}',
                        model_type = 'book',
                        allowed_parameters=['id'])

    @property
    def get_character(self):
        """ Return a single character

        :param id: the id of the character
        :return: Character object
        """
        return bind_api(api=self,
                        path='/characters/{id}',
                        model_type='character',
                        allowed_parameters=['id'])

    @property
    def get_house(self):
        """ Return a single house

        :param id: the id of the house
        :return: House object
        """
        return bind_api(api=self,
                        path='/houses/{id}',
                        model_type='house',
                        allowed_parameters=['id'])

