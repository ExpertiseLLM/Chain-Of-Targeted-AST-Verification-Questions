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
	if type(item) is dict:
		keys_to_convert = set(item.keys())
		for k in keys_to_convert:
			regex_keys[k] = item[k]
	elif type(item) is str:
		regex_keys[item] = item
	else:
		raise TypeError('item is not a dict or a string')
	return regex_keys

