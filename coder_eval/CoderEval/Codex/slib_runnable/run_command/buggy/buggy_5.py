def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	# We create a temporary file to hold the output of the commands, if we are
	# going to capture it.
	if hide_stderr:
		stderr = open(os.devnull, 'wb')
	else:
		stderr = sys.stderr

	if isinstance(commands, basestring):
		commands = [commands]
	for command in commands:
		if verbose:
			print 'Running: %s' % command
		try:
			subprocess.check_call(command, cwd=cwd, stdout=sys.stdout, stderr=stderr, shell=True, env=env)
		except subprocess.CalledProcessError as e:
			if verbose:
				print 'Command failed with exit code %d.' % e.returncode
			return e.returncode
	return 0


