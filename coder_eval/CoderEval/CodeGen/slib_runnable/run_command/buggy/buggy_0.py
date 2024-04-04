def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	if isinstance(args, str):
		args = shlex.split(args)
	if cwd is None:
		cwd = os.getcwd()
	if env is None:
		env = os.environ
	#