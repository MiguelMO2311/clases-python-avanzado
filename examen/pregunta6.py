class MyClass:
	def set_value(self, key, value):
		self._store[key] = value
		self._store.update({key: value})
