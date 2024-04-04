def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if not isinstance(commands, (list, tuple)):
		commands = [commands]
	if not cwd:
		cwd = os.getcwd()
	if not env:
		env = os.environ.copy()

	# Find the first command that works
	for command in commands:
		try:
			subprocess.check_call(
				[command] + args,
				cwd=cwd,
				stdout=(subprocess.PIPE if hide_stderr else None),
				stderr=(subprocess.PIPE if hide_stderr else None),
				env=env
			)
			return
		except (OSError, subprocess.CalledProcessError):
			pass

	# Report failure
	if verbose:
		print('Failed to execute one of the following commands:')
		for command in commands:
			print('  ' + command)

