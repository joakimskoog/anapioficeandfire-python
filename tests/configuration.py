# -*- coding: utf-8 -*-

import unittest
from anapioficeandfire import api

class AnApiOfIceAndFireTestCase(unittest.TestCase):
    def setUp(self):
        self.api = api.API()
