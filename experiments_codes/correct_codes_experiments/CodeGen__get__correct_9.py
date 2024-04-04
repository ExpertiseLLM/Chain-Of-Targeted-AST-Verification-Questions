def get(self, key, default=None):
	"""
	D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
	"""
	try: return self[key]
	except KeyError: return default
	except TypeError: return default

