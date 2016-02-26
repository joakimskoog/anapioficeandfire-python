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


    def test_get_character(self):
        jon_snow = anapioficeandfire.get_character(583)
        self.assertEquals(jon_snow.name, 'Jon Snow')


    def test_get_house(self):
        house_targaryen = anapioficeandfire.get_house(378)
        self.assertEquals(house_targaryen.name, 'House Targaryen of King\'s Landing')
