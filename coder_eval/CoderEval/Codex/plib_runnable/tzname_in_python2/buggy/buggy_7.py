def tzname_in_python2(namefunc):
	def wrapper(self, dt):
		if not PYTHON3:
			return (namefunc(self, dt)[0] or '').encode('utf-8'), \
				(namefunc(self, dt)[1] or '').encode('utf-8')
		else:
			return namefunc(self, dt)
	return wrapper

