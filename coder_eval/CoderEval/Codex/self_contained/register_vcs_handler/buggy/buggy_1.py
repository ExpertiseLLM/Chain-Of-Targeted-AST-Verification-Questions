def register_vcs_handler(vcs, method):
	vcs.handler = method
	return method

