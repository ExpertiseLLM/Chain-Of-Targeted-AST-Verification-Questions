def _dictsum(dicts):
	ret = {}
	for d in dicts:
		for k in d:
			if k in ret:
				ret[k] += d[k]
			else:
				ret[k] = d[k]
	return ret

