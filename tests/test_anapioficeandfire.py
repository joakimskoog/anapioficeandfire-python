#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_anapioficeandfire.py
----------------------------------
Tests for `anapioficeandfire` module.
"""

import unittest
from anapioficeandfire import  anapioficeandfire

from anapioficeandfire.models import (
    Book,
    Character,
    House
)

class AnApiOfIceAndFireTest(unittest.TestCase):

    def test_get_book(self):
        game_of_thrones = anapioficeandfire.get_book(1)
        self.assertEquals(game_of_thrones.name, 'A Game of Thrones')

    def test_get_book_characters(self):
        game_of_thrones = anapioficeandfire.get_book(1)

        for character in game_of_thrones.get_characters():
            if character is not None: #We don't want send thousands of requests, that would take forever
                break


    def test_get_book_pov_characters(self):
        game_of_thrones = anapioficeandfire.get_book(1)
        number_pof_pov_characters = len(list(game_of_thrones.get_pov_characters()))
        self.assertEquals(9, number_pof_pov_characters)


    def test_get_character(self):
        jon_snow = anapioficeandfire.get_character(583)
        self.assertEquals(jon_snow.name, 'Jon Snow')


    def test_get_character_allegiances(self):
        catelyn_stark = anapioficeandfire.get_character(232)
        number_of_allegiances = len(list(catelyn_stark.get_allegiances()))
        self.assertEquals(2, number_of_allegiances)


    def test_get_character_books(self):
        catelyn_stark = anapioficeandfire.get_character(232)
        number_of_books = len(list(catelyn_stark.get_books()))
        self.assertGreater(number_of_books, 0)


    def test_get_character_pov_books(self):
        catelyn_stark = anapioficeandfire.get_character(232)
        number_of_pov_books = len(list(catelyn_stark.get_pov_books()))
        self.assertEquals(3, number_of_pov_books)


    def test_get_house(self):
        house_targaryen = anapioficeandfire.get_house(378)
        self.assertEquals(house_targaryen.name, 'House Targaryen of King\'s Landing')


    def test_get_house_current_lord(self):
        house_baelish = anapioficeandfire.get_house(10)
        current_lord = house_baelish.get_current_lord()

        self.assertEquals('Petyr Baelish', current_lord.name)


    def test_get_house_heir(self):
        house_tarly = anapioficeandfire.get_house(379)
        heir = house_tarly.get_heir()

        self.assertEquals('Dickon Tarly', heir.name)


    def test_get_house_overlord(self):
        house_tarly = anapioficeandfire.get_house(379)
        overlord = house_tarly.get_overlord()

        self.assertEquals('House Tyrell of Highgarden', overlord.name)


    def test_get_house_founder(self):
        house_stark = anapioficeandfire.get_house(362)
        founder = house_stark.get_founder()

        self.assertEquals('Brandon Stark', founder.name)


    def test_get_house_cadet_branches(self):
        house_kenning = anapioficeandfire.get_house(218)
        number_of_cadet_branches = len(list(house_kenning.get_cadet_branches()))

        self.assertGreater(number_of_cadet_branches, 0)


    def test_get_house_sworn_members(self):
        house_kenning = anapioficeandfire.get_house(218)
        number_of_sworn_members = len(list(house_kenning.get_sworn_members()))

        self.assertGreater(number_of_sworn_members, 0)
