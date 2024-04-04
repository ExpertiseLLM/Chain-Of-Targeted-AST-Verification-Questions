def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	success = True
	for index, cmd in enumerate(commands):
		try:
			out = subprocess.check_output(cmd, cwd=cwd, stderr=subprocess.STDOUT, env=env)
		except subprocess.CalledProcessError as exc:
			out = exc.output
			if verbose:
				print(f'command {cmd!r} failed with error output: {exc}')
				print(f'output was {out!r}')
			success = False
		except OSError:
			success = False
			if hide_stderr:
				out = 'command output'
		if success:
			break
	if success:
		return out
	assert False, "subprocess.check_output failed with error output"