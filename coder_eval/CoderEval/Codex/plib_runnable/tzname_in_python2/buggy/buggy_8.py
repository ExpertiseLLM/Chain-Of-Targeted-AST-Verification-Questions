def tzname_in_python2(namefunc):
	def newfunc(dt):
		rv = namefunc(dt)
		if not isinstance(rv, str):
			return rv.encode('utf-8')
		return rv
	return newfunc

