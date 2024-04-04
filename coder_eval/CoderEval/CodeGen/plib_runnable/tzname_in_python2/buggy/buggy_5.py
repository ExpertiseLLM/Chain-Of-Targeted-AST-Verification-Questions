def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2

tzname() API changed in Python 3. It used to return bytes, but was changed
to unicode strings
	"""
	if PY3:
		def tzname_in_python3(name):
			return name.encode('utf-8')
	else:
		def tzname_in_python3(name):
			return name
	def new_name(name):
		try:
			return name.encode('utf-8')
		except UnicodeEncodeError:
			return name.encode('latin-1')
	def tzname_in_python2(name):
		try:
			return name.encode('utf-8')
		except UnicodeEncodeError:
			return name.encode('latin-1')
	def tzname_in_python3(name):
		try:
			return name.encode('utf-8')
		except UnicodeEncodeError:
			return name.encode('latin-1')
	return tzname_in_python2, new_name, tzname_in_python3
tzname_in_python2, tzname_in_python3, tzname_in_python2 = tzname_in_python3 = tzname_in_python2 = lambda name: name
