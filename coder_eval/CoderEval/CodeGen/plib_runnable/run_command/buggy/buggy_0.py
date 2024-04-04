def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	if isinstance(args, six.string_types):
		args = shlex.split(args, True)
	if cookiecutter.is_eager():
		#