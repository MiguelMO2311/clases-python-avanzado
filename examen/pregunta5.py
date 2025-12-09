class SomeClass:
    def some_method(self):
        if self._i >= len(self._data):
            raise StopIteration
