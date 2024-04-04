def tzname_in_python2(namefunc):
	import sys
	if sys.version_info[0] == 2:
		def tzname_in_python2_wrapper(*args, **kwargs):
			return [str(i) for i in namefunc(*args, **kwargs)]
		return tzname_in_python2_wrapper
	return namefunc

