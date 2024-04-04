def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	success = True
	for index, cmd in enumerate(commands):
		try:
			out = run_command(cmd, args, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)
			success = success and out.success
		except CliError as exception:
			out = exception
			if hide_stderr:
				out.stderr = None
				out.stdout = None
			logger.error(to_native(out))
			success = success and not exception.errno
			if success:
				break
		if success:
			break
		if (index + 1) >= len(commands):
			break
	return success, out