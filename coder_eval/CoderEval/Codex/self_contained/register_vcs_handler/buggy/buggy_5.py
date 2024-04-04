def register_vcs_handler(vcs, method):
	def wrapper(func):
		global VCS_HANDLERS
		VCS_HANDLERS[vcs] = (func, method)
		return func
	return wrapper


