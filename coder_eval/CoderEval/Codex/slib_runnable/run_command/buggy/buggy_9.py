def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if isinstance(commands, str):
		commands = [commands]

	if env is None:
		env = environ.copy()
	else:
		env = env.copy()

	if 'PATH' in env:
		env['PATH'] = env['PATH'].split(':')
	else:
		env['PATH'] = os.environ['PATH'].split(':')

	try:
		os.unsetenv('LD_LIBRARY_PATH')
	except AttributeError:
		pass

	try:
		os.unsetenv('DYLD_LIBRARY_PATH')
	except AttributeError:
		pass

	if not verbose:
		stdout = stderr = open(devnull, 'wb')
	elif hide_stderr:
		stdout = sys.stdout
		stderr = open(devnull, 'wb')
	else:
		stdout = sys.stdout
		stderr = sys.stderr

	for command in
