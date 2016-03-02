# -*- coding: utf-8 -*-

import requests
import re

try:
    from urllib.parse import quote
    from anapioficeandfire.error import AnApiOfIceAndFireError
    from anapioficeandfire.utils import convert_to_utf8_str
    from anapioficeandfire.utils import to_camel_case
except:
    from urllib import quote
    from error import AnApiOfIceAndFireError
    from utils import convert_to_utf8_str
    from utils import to_camel_case

re_path_template = re.compile('{\w+}')

def bind_api(**config):

    class APIRequest(object):
        api = config['api']
        path = config['path']
        allowed_parameters = config.get('allowed_parameters', [])
        method = config.get('method', 'GET')
        is_data_list = config.get('is_data_list', False)
        model_type = config.get('model_type', None)
        iteration_mode = config.get('iteration_mode', None)
        session = requests.Session()

        def __init__(self, kwargs):
            self.parser = kwargs.pop('parser', self.api.parser)

            #Set the header so that we can get statistics on the usage
            self.session.headers['User-Agent'] = 'anapioficeandfire-python'

            #Set the Accept header to show the API that we want to use version 1 of the API.
            self.session.headers['Accept'] ='application/vnd.anapioficeandfire+json; version={0}'.format(self.api.api_version)

            self.build_parameters(kwargs)
            self.build_path()

        def build_parameters(self, kwargs):
            for key, value in kwargs.items():
                if value is None:
                    continue
                try:
                    if key in self.allowed_parameters:

                        #We need to convert parameter keys to camelCase because the API uses camelCase convention
                        camel_case_key = to_camel_case(key)
                        self.session.params[camel_case_key] = convert_to_utf8_str(value)
                except IndexError:
                    raise AnApiOfIceAndFireError('Invalid parameters supplied')

        def build_path(self):
            for variable in re_path_template.findall(self.path):
                name = variable.strip('{}')
                try:
                    value = quote(self.session.params[name])
                except KeyError:
                    raise AnApiOfIceAndFireError('No parameter value found for path variable: %s' % name)

                #Remove the parameter since it won't be used as an URL parameter
                del self.session.params[name]
                self.path = self.path.replace(variable, value)

        def execute(self):
            url = 'http://{0}{1}'.format(self.api.host, self.path)

            try:
                response = self.session.request(self.method, url)
            except Exception as e:
                raise AnApiOfIceAndFireError('Failed to send request')

            result = self.parser.parse(self, response.text)

            return result

    def _call(*args, **kwargs):
        request = APIRequest(kwargs)

        return request.execute()


    if APIRequest.iteration_mode == 'id':
        _call.iteration_mode = 'id'
    elif  APIRequest.iteration_mode == 'page':
        _call.iteration_mode = 'page'


    return _call
