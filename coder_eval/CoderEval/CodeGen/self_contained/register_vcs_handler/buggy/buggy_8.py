def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def decorator(func):
		def wrapper(vcs, *args, **kwargs):
			if vcs == 'git':
				if method not in ('export', 'import'):
					raise ValueError('Invalid VCS method')
			else:
				raise NotImplementedError('This VCS does not support %s' % vcs)
			return func(vcs, *args, **kwargs)
		return wrapper
	return decorator