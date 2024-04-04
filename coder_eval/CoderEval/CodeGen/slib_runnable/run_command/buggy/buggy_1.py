def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	success = True
	for cmd in commands:
		try:
			if args is None:
				output = cmd(options, cwd=cwd)
			else:
				output = cmd(options, args, cwd=cwd)
		except PipToolsError as e:
			logger.error(e)
			success = False
		if not output:
			success = False
			break
	return success

