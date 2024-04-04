def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(handler):
		handler.VCS = vcs
		handler.method = method
		return handler
	return decorator

