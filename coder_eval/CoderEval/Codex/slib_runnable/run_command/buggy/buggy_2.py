def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if not isinstance(commands, (list, tuple)):
		commands = [commands]
	for command in commands:
		if verbose:
			print 'Running command: %s %s' % (command, args)
		if hide_stderr:
			with open(os.devnull, 'w') as devnull:
				subprocess.check_call([command] + args, cwd=cwd, stdout=devnull, stderr=devnull, env=env)
		else:
			subprocess.check_call([command] + args, cwd=cwd, env=env)


