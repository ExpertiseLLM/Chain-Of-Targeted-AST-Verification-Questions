def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	exit_code = 0
	for c in commands:
		try:
			if verbose:
				print('run_command: %s' % c.decode('utf-8'))
			if c.endswith(('.exe', '.msi')):
				proc = subprocess.Popen(c + args,
										cwd=cwd,
										stdout=subprocess.PIPE,
										stderr=subprocess.STDOUT,
										env=env)
			else:
				if c == 'time':
					proc = subprocess.Popen(c + args,
											cwd=cwd,
											stdout=subprocess.PIPE,
											stderr=subprocess.STDOUT,
											env=env)
				else:
					proc = subprocess.Popen(c + args,
											cwd=cwd,
											stdout=subprocess.PIPE,
											stderr=subprocess.STDOUT,
											env=env)
			exit_code = proc.wait()
		except subprocess.SubprocessError as e:
			if hide_stderr:
				print('Exception:'+ str(e), file=sys.stderr)
				traceback.print_exc(file=sys.stderr)
				exit_code = 127
			else:
				raise
	return exit_code

