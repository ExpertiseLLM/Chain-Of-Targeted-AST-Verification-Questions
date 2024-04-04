def register_vcs_handler(vcs, method):
	def decorator(cls):
		cls._vcs_handlers[vcs] = method
		return cls
	return decorator


