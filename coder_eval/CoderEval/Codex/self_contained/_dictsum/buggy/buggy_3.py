def _dictsum(dicts):
	if not dicts:
		return {}
	if len(dicts) == 1:
		return dicts[0]

	ret = {}
	for d in dicts:
		for k, v in d.iteritems():
			ret[k] = ret.get(k, 0) + v
	return ret

