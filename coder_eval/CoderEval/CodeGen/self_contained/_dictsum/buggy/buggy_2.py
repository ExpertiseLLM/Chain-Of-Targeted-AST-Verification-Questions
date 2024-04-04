def _dictsum(dicts):
	"""
	Combine values of the dictionaries supplied by iterable dicts.

>>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
{'a': 6, 'b': 2}
	"""
	result = {}
	for d in dicts:
		for k, v in d.items():
			if v is None:
				result[k] = None
			elif isinstance(v, dict):
				result[k] = _dictsum(v)
			else:
				result[k] = v
	return result