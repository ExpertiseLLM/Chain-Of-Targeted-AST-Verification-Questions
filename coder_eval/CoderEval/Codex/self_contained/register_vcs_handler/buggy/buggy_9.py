def register_vcs_handler(vcs, method):
	if not isinstance(vcs, (list, tuple)):
		vcs = [vcs]
	def register(func):
		for v in vcs:
			_vcs_handlers[v][method] = func
		return func
	return register

