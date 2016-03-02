# -*- coding: utf-8 -*-

class AnApiOfIceAndFireError(Exception):

    def __init__(self, reason, response=None):
        self.reason = response
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason
