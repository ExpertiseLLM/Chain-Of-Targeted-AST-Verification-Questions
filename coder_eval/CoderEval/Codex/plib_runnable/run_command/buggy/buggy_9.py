def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if not isinstance(commands, list):
		commands = [commands]
	stdout_text = None
	for command in commands:
		if verbose:
			print("Running command: {0} {1}".format(command, args))
		try:
			stdout_text = subprocess.check_output(
				[command] + args,
				stderr=subprocess.STDOUT,
				cwd=cwd,
				env=env
			)
		except subprocess.CalledProcessError as e:
			if verbose or not hide_stderr:
				print("Command failed: {0} {1}".format(command, args))
				print(e.output)
				print("")
			continue
		else:
			if verbose:
				print("Command succeeded: {0} {1}".format(command, args))
			break
	return stdout
