def get(self, key, default=None):
	"""
	D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
	"""
	try:
		if key in self:
			return self[key]
		else:
			return default
	except KeyError:
		return default

	return default

