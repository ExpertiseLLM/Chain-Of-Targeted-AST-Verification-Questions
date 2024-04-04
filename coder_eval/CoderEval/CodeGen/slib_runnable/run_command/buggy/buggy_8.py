def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	assert isinstance(args, (list, tuple))
	cmds = []
	for c in commands:
		assert isinstance(c, (str, unicode))
		#