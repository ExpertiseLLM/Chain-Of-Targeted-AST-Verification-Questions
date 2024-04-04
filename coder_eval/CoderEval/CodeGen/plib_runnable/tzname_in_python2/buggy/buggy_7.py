def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2

tzname() API changed in Python 3. It used to return bytes, but was changed
to unicode strings
	"""
	def tzname_in_python3(name):
		if name in ("GMT", "UTC"):
			return name
		name = name.encode("ascii", "ignore")
		if name.endswith(b'-W/'):
			name = name[:-4]
		if name.endswith(b'-W'):
			name = name[:-2]
		if name.endswith(b'+W/'):
			name = name[:-4]
		if name.endswith(b'+'):
			name = name[:-1]
		return name
	return tzname_in_python3

_import_tzinfo_gen = gen_tzinfo_codes(timezone.all_timezones)
_tzinfo_code_map = dict([(code, name)
	for code, name in _import_tzinfo_gen])

