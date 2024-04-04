def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		if vcs not in VcsHandler:
			raise Exception("Unsupported VCS '%s'" % vcs)
		VcsHandler[vcs].append(method)
		return func
	return decorator