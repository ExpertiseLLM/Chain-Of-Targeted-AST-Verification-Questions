def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		setattr(func, '_may_be_handler', method)
		return func
	return decorator