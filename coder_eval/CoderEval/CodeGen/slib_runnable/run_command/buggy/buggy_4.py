def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	process = None
	for command in commands:
		try:
			process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
			exit_code = process.wait()
			if exit_code:
				if verbose:
					print('failed: %s' % (' '.join(command)))
					print(process.stderr.read().decode('utf-8'))
				raise Exception("command '%s' failed with exit code %d" % (' '.join(command), exit_code))
		except OSError:
			e = sys.exc_info()[1]
			if e.errno == errno.ENOENT:
				continue
			elif e.errno == errno.EPIPE:
				continue
			else:
				raise

	if process:
		wait = functools.partial(process.wait, max_wait=60)
		while wait():
			pass  #