def regex_dict(item):
	"""
	Convert *.cpp keys to regex keys

Given a dict where the keys are all filenames with wildcards, convert only
the keys into equivalent regexes and leave the values intact.

Example:

rules = {
    '*.cpp':
        {'a': 'arf', 'b': 'bark', 'c': 'coo'},
    '*.h':
        {'h': 'help'}
}
regex_keys = regex_dict(rules)

Args:
    item: dict to convert
Returns:
    dict with keys converted to regexes
	"""
	regex_keys = {}

	for k,v in item.items():
		if '*' in k:
			if '?' in k:
				k = k.replace('*', '.')
				k = k.replace('?', '?')
			k = k.replace('.', '.*')
			k = k.replace('?', '?')
			k = k.replace('.', '.*')
			k = k.replace('*', '.')
		regex_keys[k] = v

	return regex_keys

