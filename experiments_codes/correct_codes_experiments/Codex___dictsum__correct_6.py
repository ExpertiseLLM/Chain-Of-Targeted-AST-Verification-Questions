def _dictsum(dicts):
	result = {}
	for d in dicts:
		for k, v in d.items():
			result[k] = v + result.get(k, 0)
	return result

