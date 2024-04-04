def register_vcs_handler(vcs, method):
	vcs_handlers[vcs] = method
	return method

