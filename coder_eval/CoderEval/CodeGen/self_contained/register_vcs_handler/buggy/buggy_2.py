def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		if vcs in ['git','svn']:
			if hasattr(func, 'VCS'):
				raise ValueError('%s is already a handler for a VCS' % vcs)
			setattr(func, vcs, True)
		return func
	return decorator

