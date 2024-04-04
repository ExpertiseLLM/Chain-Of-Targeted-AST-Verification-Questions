def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, (list, tuple))
	p = None
	for c in commands:
		try:
			# remember shell=False, so use git.cmd on windows, not just git
			p = Popen(c, cwd=cwd, stdout=PIPE, stderr=(PIPE if hide_stderr else None), shell=True, env=env)
			break
		except EnvironmentError:
			e = sys.exc_info()[1]
			if e.errno == errno.ENOENT:
				pass
			else:
				if verbose:
					print("unable to run command %s" % c)
				raise
	if p is None:
		if verbose:
			print("no command %s found" % commands[0])
		return None, None
	stdout = p.communicate()[0].strip()
	return stdout.decode('utf-8'), p.
