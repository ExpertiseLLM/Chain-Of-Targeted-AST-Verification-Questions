def tzname_in_python2(namefunc):
	def wrapper(*args, **kwargs):
		result = namefunc(*args, **kwargs)
		if not isinstance(result, str):
			result = result.encode('utf-8')
		return result
	return wrapper

