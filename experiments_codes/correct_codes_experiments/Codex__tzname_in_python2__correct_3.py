def tzname_in_python2(namefunc):
	if sys.version_info.major == 2:
		def tzname_in_python2_decorator(self, *args, **kwargs):
			name = namefunc(self, *args, **kwargs)
			return name.encode('utf-8')
		return tzname_in_python2_decorator
	return namefunc


