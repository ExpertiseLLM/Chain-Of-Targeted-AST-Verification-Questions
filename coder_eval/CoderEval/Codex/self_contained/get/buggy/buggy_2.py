def get(self, key, default=None):
	return self.get_or_default(key, default)

	def get_or_default(self, key, default):
		try:
			return self.get_by_key(key)
		except KeyError:
			return default

	def get_by_key(self, key):
		try:
			return self.__dict__[key]
		except KeyError:
			return self.__dict__[key.lower()]

	def __getitem__(self, key):
		return self.get_by_key(key)

	def __setitem__(self, key, value):
		self.__dict__[key] = value

	def keys(self):
		return self.__dict__.keys()

	def values(self):
		return self.__dict__.values()

	def items(self):
		return self.__dict__.items()

	def __contains__(self, key):
		return key in self.__dict__ or key.lower() in self.
