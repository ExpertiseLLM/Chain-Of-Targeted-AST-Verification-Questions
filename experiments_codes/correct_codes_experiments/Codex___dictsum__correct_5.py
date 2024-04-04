def _dictsum(dicts):
	if not dicts:
		return {}
	result = {}
	for d in dicts:
		for k, v in d.items():
			result[k] = result.get(k, 0) + v
	return result

