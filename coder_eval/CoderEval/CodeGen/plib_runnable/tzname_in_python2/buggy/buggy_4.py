def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2

tzname() API changed in Python 3. It used to return bytes, but was changed
to unicode strings
	"""
	def new_namefunc(name):
		if name is not None:
			name = name.encode('utf-8')
		return name.decode('utf-8')
	return new_namefunc
tzname_in_python2 = tzname_in_python3 = tzname_in_python2(tzname)

