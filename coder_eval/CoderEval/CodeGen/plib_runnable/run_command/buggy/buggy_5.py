def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list), "The 'commands' argument must be a list of strings (commands to run)"
	assert all([isinstance(cmd, (str, unicode)) for cmd in commands]), "The 'commands' argument must be a list of strings (commands to run)"

	#