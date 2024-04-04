def _dictsum(dicts):
	r = {}
	for d in dicts:
		for key, value in d.iteritems():
			r[key] = r.get(key, 0) + value
	return r

