def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	exit_code = 0
	for cmd in commands:
		try:
			if args is None:
				p = subprocess.Popen(
					cmd, shell=True,
					stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
					cwd=cwd)
			else:
				p = subprocess.Popen(
					cmd, shell=True,
					stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
					cwd=cwd, env=env)
			(stdout, stderr) = p.communicate()
			if p.returncode!= 0:
				if stdout:
					logger.error('Running command %s failed with exit status %s and output:\n%s',
						cmd, p.returncode, stdout.decode('utf-8'))
				if stderr:
					logger.error('Running command %s failed with exit status %s and error:\n%s',
						cmd, p.returncode, stderr.decode('utf-8'))
				exit_code = p.returncode
		except Exception as e:
			logger.error('Running command %s failed with exception %s', cmd, e)
			if traceback.print_exc(file=sys.stdout) or hide_stderr:
				traceback.print_exc(file=sys.stdout)
			exit_code = 128 + p.returncode
	sys.exit(exit_code)

