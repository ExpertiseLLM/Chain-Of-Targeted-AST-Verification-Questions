def tzname_in_python2(namefunc):
	def tzname_in_python2_decorator(self, dt):
		tzname = namefunc(self, dt)
		if isinstance(tzname, six.text_type):
			tzname = tzname.encode("utf-8")
		return tzname
	return tzname_in_python2_decorator


