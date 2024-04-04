def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if isinstance(commands, str):
		commands = [commands]
	
	if env is None:
		env = {}
	
	for command in commands:
		try:
			command_env = os.environ.copy()
			command_env.update(env)
			if verbose:
				print 'Running command: "'+command+'"'
			if sys.platform == 'win32':
				# Use shell=True on Windows, so shell-specific commands like "dir" work.
				shell = True
			else:
				shell = False
			if hide_stderr:
				stderr = open(os.devnull, 'w')
			else:
				stderr = None
			subprocess.check_output(command, stderr=stderr, env=command_env, shell=shell, cwd=cwd)
		except:
			print 'Failed command:
