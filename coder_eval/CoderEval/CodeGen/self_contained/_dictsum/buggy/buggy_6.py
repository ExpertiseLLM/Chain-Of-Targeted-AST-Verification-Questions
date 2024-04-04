def _dictsum(dicts):
	"""
	Combine values of the dictionaries supplied by iterable dicts.

>>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
{'a': 6, 'b': 2}
	"""
	for d in dicts:
		for k, v in d.items():
			if isinstance(v, dict):
				d[k] = _dictsum(v)
			elif v is None:
				d[k] = None
			else:
				d[k] = v
	return dicts

