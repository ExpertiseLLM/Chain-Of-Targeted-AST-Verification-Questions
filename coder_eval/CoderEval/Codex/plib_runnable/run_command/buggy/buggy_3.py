def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	try:
		# If commands is a string then we just call it as is
		if isinstance(commands, str):
			stdout = check_output(commands, cwd=cwd, stderr=STDOUT, env=env)
			stdout = stdout.decode()
			if verbose:
				print(stdout)
			return stdout

		# If commands is a list then we assume the first one is the command,
		# and the rest are arguments.
		if isinstance(commands, list):
			args = commands[1:] + args
			commands = commands[0]
			if verbose:
				print('Executing:', commands, args)
			p = Popen([commands] + args, cwd=cwd, stdout=PIPE, stderr=(PIPE if hide_stderr else None), env=env)
			output, stderr = p.communicate()
			if p.return
