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


def get_all_books(name, from_release_date, to_release_date):
    return None


def get_book(book_id):
    ''' Return a single book '''
    result = _get(book_id, 'books')
    return Book(result.content)


def get_all_characters(name, culture, born, died, is_alive):
    return None


def get_character(character_id):
    ''' Return a single character '''
    result = _get(character_id, 'characters')
    return Character(result.content)


def get_all_houses(name, region, words, has_words, has_titles, has_seats, has_died_out, has_ancestral_weapons):
    return None


def get_house(house_id):
    ''' Return a single house '''
    result = _get(house_id, 'houses')
    return House(result.content)


