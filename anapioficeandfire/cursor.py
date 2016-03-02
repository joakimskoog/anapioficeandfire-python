# -*- coding: utf-8 -*-

try:
    from anapioficeandfire.error import AnApiOfIceAndFireError
except:
    from error import AnApiOfIceAndFireEror

class Cursor(object):

    def __init__(self, method, **kwargs):
        if hasattr(method, 'iteration_mode'):
            if method.iteration_mode == 'id':
                self.iterator = IdIterator(method, kwargs)
            elif method.iteration_mode == 'page':
                self.iterator = PageIterator(method, kwargs)
            else:
                raise AnApiOfIceAndFireError('Invalid iteration mode')
        else:
            raise AnApiOfIceAndFireError('This method does not pagination')

    def items(self, limit=0):
        """ Return iterator for IDs

        :param limit: the number of items that should be returned
        :return:
        """
        if limit > 0:
            self.iterator.limit = limit

        if type(self.iterator) is not IdIterator:
            raise AnApiOfIceAndFireError('This method does not support iterating over IDs')

        return self.iterator

    def pages(self, limit=0):
        """ Return iterator for pages

        :param limit: the number of pages that should be returned
        :return:
        """

        if limit > 0:
            self.iterator.limit = limit

        if type(self.iterator) is not PageIterator:
            raise AnApiOfIceAndFireError('This method does not support iterating over pages')

        return self.iterator



class IdIterator(object):

    def __init__(self, method, kwargs):
        self.method = method
        self.kwargs = kwargs
        self.ids = kwargs.pop('ids', [])
        self.total_number_of_ids = len(self.ids)
        self.limit = 0

    def __iter__(self):
        self.current_index = 0
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self.limit > 0 and self.current_index > self.limit:
            raise StopIteration

        if self.current_index == self.total_number_of_ids:
            raise StopIteration

        model = self.method(id=self.ids[self.current_index])

        self.current_index += 1
        return model


class PageIterator(object):

    def __init__(self, method, kwargs):
        self.method = method
        self.kwargs = kwargs
        self.limit = 0

    def __iter__(self):
        self.current_page = 1
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self.limit > 0 and self.current_page > self.limit:
            raise StopIteration

        items = self.method(page=self.current_page, **self.kwargs)
        if len(items) == 0:
            raise StopIteration
        self.current_page += 1

        return items
