# -*- coding: utf-8 -*-

try:
    from anapioficeandfire.models import (
        Book,
        Character,
        House
    )
    from anapioficeandfire.utils import query
    from anapioficeandfire import settings
except:
    import settings
    from models import (
        Book,
        Character,
        House
    )
    from utils import query


def _get(id, model_type):
    result = query("{0}/{1}/{2}".format(settings.API_BASE_URL, model_type,str(id)))
    return result

def get_book(book_id):
    ''' Return a single book '''
    result = _get(book_id, "books")
    return Book(result.content)


def get_character(character_id):
    ''' Return a single character '''
    return None


def get_house(house_id):
    ''' Return a single house '''
    return None


