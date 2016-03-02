# -*- coding: utf-8 -*-

import ujson as json

try:
    from anapioficeandfire.error import AnApiOfIceAndFireError
except:
    from error import AnApiOfIceAndFireError


class JSONParser(object):

    def parse(self, method, data):
        try:
            json_data = json.loads(data)
            return json_data
        except Exception:
            raise AnApiOfIceAndFireError('Failed to parse JSON data')


class ModelParser(JSONParser):

    def __init__(self, model_factory):
        JSONParser.__init__(self)
        self.model_factory = model_factory

    def parse(self, method, data):
        if method.model_type is None:
            return
        model = self.model_factory.create(method.model_type)
        if model is None:
            raise AnApiOfIceAndFireError('No model for the type: ' + method.model_type)


        json = JSONParser.parse(self, method, data)

        if method.is_data_list:
            return model.parse_list(method.api, json)
        else:
            return model.parse(method.api, json)



