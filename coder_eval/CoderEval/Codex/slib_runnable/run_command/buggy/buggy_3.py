def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	try:
		if not cwd:
			cwd = os.getcwd()
		if not isinstance(commands, list):
			commands = [commands]
		if not isinstance(args, list):
			args = [args]
		# TODO: subprocess.check_call() actually does not work
		# with some commands, so we use subprocess.Popen() instead.
		process = subprocess.Popen(commands + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
		output, error = process.communicate()
		# TODO: this is a hack to get rid of the '\r' character on Windows
		if not verbose:
			output = output.replace('\r', '')
			error = error.replace('\r', '')
		if error and not hide_stderr:
			print 'ERROR: %s' % error.strip()
	
