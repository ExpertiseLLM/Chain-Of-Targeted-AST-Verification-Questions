def get(self, key, default=None):
		return self.__dict__.get(key, default)
	
	def has_key(self, key):
	"""
	D.has_key(k) -> 1 if D.has_key(k), else 0
	"""
		return self.__dict__.has_key(key)
	
	def items(self):
	"""
	D.items() -> list of D's (key, value) pairs, as 2-tuples
	"""
		return self.__dict__.items()
	
	def iteritems(self):
	"""
	D.iteritems() -> an iterator over the (key, value) items of D
	"""
		return self.__dict__.iteritems()
	
	def iterkeys(self):
	"""
	D.iterkeys() -> an iterator over the keys of D
	"""
		return self.__dict__.iterkeys()
	
	def itervalues(self):
	"""
	D.itervalues() -> an iterator over the values of D
	"""
		return self.
