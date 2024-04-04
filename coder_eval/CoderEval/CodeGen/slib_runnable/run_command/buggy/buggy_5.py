def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	assert isinstance(args, list)
	assert isinstance(cwd, (str, os.PathLike))
	f = None  #