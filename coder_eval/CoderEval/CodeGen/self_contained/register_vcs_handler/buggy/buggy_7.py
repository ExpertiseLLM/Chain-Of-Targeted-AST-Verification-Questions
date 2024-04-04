def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	if vcs not in HANDLERS:
		HANDLERS[vcs] = {}
	try:
		HANDLERS[vcs][method.__name__] = method
	except KeyError:
		HANDLERS[vcs][method.__name__] = method.__name__
	return method

