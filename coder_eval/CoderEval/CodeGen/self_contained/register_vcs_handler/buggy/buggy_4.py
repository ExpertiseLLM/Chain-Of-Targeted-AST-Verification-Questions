def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		if hasattr(vcs, method):
			raise ValueError("Cannot register duplicate VCS handler %s" % vcs)
		setattr(vcs, method, func)
		return func
	return decorator

