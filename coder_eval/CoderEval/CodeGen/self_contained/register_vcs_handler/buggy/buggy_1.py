def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		@wraps(func)
		def decorated_function(*args, **kwargs):
			assert args
			assert not kwargs
			assert vcs in vcs_map
			assert method in vcs_map[vcs]
			assert callable(vcs_map[vcs][method])
			assert callable(func)
			assert not isinstance(args, tuple)
			assert not isinstance(kwargs, dict)
			vcs_map[vcs][method].append(func)
			return func(*args, **kwargs)
		return decorated_function
	return decorator

