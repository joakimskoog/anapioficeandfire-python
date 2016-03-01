

try:
    from anapioficeandfire.error import AnApiOfIceAndFireError
except:
    from error import AnApiOfIceAndFireEror

class Cursor(object):

    def __init__(self, method, **kwargs):
        iteration_mode = kwargs.get('iteration_mode', None)
        if iteration_mode == 'url':
            self.iterator = UrlIterator(method, kwargs)
        else:
            raise AnApiOfIceAndFireError('This method does not pagination')

    def items(self, limit=0):
        ''' Return iterator for URLs '''
        if limit > 0:
            self.iterator.limit = limit

        if type(self.iterator) is not UrlIterator:
            raise AnApiOfIceAndFireError('This method does not support iterating over URLs')

        return self.iterator


class UrlIterator(object):

    def __init__(self, method, kwargs):
        self.method = method
        self.kwargs = kwargs
        self.ids = kwargs.pop('ids', [])
        self.total_number_of_ids = len(self.ids)

    def __iter__(self):
        self.current_index = 0
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        if self.current_index == self.total_number_of_ids:
            raise StopIteration

        model = self.method(id=self.ids[self.current_index])

        self.current_index += 1
        return model
