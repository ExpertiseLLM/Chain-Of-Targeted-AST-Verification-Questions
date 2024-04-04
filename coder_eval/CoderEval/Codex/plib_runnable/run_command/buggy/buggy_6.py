def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	# Make sure its a list
	if isinstance(commands, str):
		commands = [commands]
	# Merge the command and args
	commands = [commands[0] + " " + args] + commands[1:]
	if env is None:
		env = os.environ.copy()
	env['PATH'] = os.environ['PATH']
	# Call the command(s)
	for command in commands:
		if verbose:
			print("Running: " + command)
		if cwd:
			if hide_stderr:
				p = subprocess.Popen(command, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			else:
				p = subprocess.Popen(command, cwd=cwd, env=env)
		else:
			if hide_stderr:
				p = subprocess.Popen(command, env=env, std
