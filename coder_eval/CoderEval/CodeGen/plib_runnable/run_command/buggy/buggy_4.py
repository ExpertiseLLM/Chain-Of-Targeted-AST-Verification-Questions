def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	exit_code = 0
	for command in commands:
		try:
			if command.startswith('rm:') and os.path.exists(command[2:]):
				command = command[2:]
			return_code = subprocess.call(command, cwd=cwd, env=env)
		except OSError:
			e = sys.exc_info()[1]
			if hide_stderr:
				log.error('Error: %s' % str(e))
			else:
				log.error('Error while executing: %s' % command)
				log.debug(str(e))
			exit_code = 1
		except KeyboardInterrupt:
			log.error('Operation aborted by user')
			exit_code = 130
		if exit_code:
			log.debug('Operation exited with code %d' % exit_code)
			break
	return (exit_code, return_code, commands)

