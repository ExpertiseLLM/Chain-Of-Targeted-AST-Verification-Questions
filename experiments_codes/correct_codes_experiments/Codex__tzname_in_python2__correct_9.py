def tzname_in_python2(namefunc):
	def wrapper(*args, **kwargs):
		ret = namefunc(*args, **kwargs)
		if sys.version_info[0] < 3:
			ret = [x.encode('utf-8') for x in ret]
		return ret
	return wrapper

