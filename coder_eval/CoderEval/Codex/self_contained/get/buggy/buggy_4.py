def get(self, key, default=None):
	try:
		return self[key]
	except KeyError:
		return default

	def has_key(self, key):
		try:
			value = self[key]
		except KeyError:
			return False
		return True

	def items(self):
		"""
		D.items() -> list of D's (key, value) pairs, as 2-tuples
		"""
		return zip(self.keys(), self.values())

	def iteritems(self):
		"""
		D.iteritems() -> an iterator over the (key, value) items of D
		"""
		for key in self.keys():
			yield (key, self[key])

	def iterkeys(self):
		"""
		D.iterkeys() -> an iterator over the keys of D
		"""
		return self.keys().__iter__()

	def itervalues(self):
		"""
		D.itervalues() -> an iterator over the values of D
	
