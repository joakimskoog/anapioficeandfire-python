# -*- coding: utf-8 -*-

import requests
import ujson

def query(query):
    headers = {'User-Agent': 'anapioficeandfire-python'}
    response = requests.get(query, headers=headers)

    return response


