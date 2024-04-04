def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, (list, tuple))

	popen_kwargs = dict(
		stdout=subprocess.PIPE,
		stderr=(subprocess.PIPE if hide_stderr else None),
		cwd=cwd,
		env=env,
	)
	if os.name == 'nt':
		popen_kwargs['shell'] = True

	for command in commands:
		command_line = command % args
		if verbose:
			print command_line

		try:
			child = subprocess.Popen(command_line, **popen_kwargs)
		except OSError, e:
			if e.errno == 2:
				sys.stderr.write('Error: Command "%s" is not installed or not in the path.\n' % command[0])
				sys.exit(1)
			else:
				raise

		output = child.communicate()[0]
	
