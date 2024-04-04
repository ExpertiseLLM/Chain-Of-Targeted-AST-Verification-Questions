def register_vcs_handler(vcs, method):
	def decorator(f):
		f.vcs_handler = vcs
		f.vcs_method = method
		return f
	return decorator

