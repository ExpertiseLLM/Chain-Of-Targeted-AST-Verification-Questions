def register_vcs_handler(vcs, method):
	def _register_vcs_handler(func):
		_vcs_handlers[vcs] = func
		return func
	return _register_vcs_handler

