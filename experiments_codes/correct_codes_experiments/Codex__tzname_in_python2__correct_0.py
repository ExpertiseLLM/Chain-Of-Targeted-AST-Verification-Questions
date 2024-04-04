def tzname_in_python2(namefunc):
	if not PY2:
		return namefunc

	def newnamefunc(self, dt):
		name = namefunc(self, dt)
		if isinstance(name, text_type):
			name = name.encode('ascii')
		return name
	return newnamefunc


