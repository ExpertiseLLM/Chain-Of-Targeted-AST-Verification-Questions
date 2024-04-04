def _dictsum(dicts):
	d = {}
	for k in dicts[0]:
		d[k] = sum(d.get(k, 0) + dic.get(k, 0) for dic in dicts)
	return d

