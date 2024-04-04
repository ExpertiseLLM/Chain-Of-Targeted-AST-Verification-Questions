def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		vcs.register_handler(vcs, method, func)
		return func
	return decorator

