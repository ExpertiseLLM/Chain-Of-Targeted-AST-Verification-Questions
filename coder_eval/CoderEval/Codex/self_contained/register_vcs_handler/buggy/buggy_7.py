def register_vcs_handler(vcs, method):
	def wrapper(method):
		vcs_handlers[vcs] = method
		return method
	return wrapper


