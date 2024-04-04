def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	successes, errors = [], []
	if args:
		if isinstance(args, str):
			args = [args]
		for command in commands:
			try:
				if verbose:
					print('Running %s' %''.join(command + args))
				output = subprocess.check_output(command + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
			except Exception as e:
				if len(args) == 1:
					print('ERROR: %s' % e)
				else:
					print('ERROR: %s' %''.join(command + args))
				errors.append(e)
				continue
			if output:
				successes.append(command + args + [output.strip()])
	else:
		for command in commands:
			try:
				if verbose:
					print('Running %s' % (' '.join(command)))
				output = subprocess.check_output(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
			except Exception as e:
				if len(args) == 1:
					print('ERROR: %s' % e)
				else:
					print('ERROR: %s' %''.join(command))
				errors.append(e)
				continue
			if output:
				successes.append(command + [output.strip()])
	return successes, errors