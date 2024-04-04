def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	# If we have a list of commands, we need to combine them into a single string
	if isinstance(commands, (list, tuple)):
		commands = " ".join(commands)

	# If we have a list of arguments, we need to combine them into a single string
	if isinstance(args, (list, tuple)):
		args = " ".join(args)

	# Make sure we have a string
	assert isinstance(commands, str) and isinstance(args, str)

	# Construct the command string
	command = '%s %s' % (commands, args)

	if verbose:
		print(command)

	# Execute the command
	subprocess.check_call(command, cwd=cwd, shell=True, stderr=(subprocess.STDOUT if hide_stderr else None), env=env)

