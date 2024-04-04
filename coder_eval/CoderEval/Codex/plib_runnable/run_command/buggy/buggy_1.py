def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, (list, tuple))
	popen_kwargs = dict(
		stdout=PIPE,
		stderr=(DEVNULL if hide_stderr else PIPE),
		cwd=cwd,
		env=env,
	)
	if os.name == 'nt':
		popen_kwargs['creationflags'] = 0x08000000  # CREATE_NO_WINDOW

	for cmd in commands:
		try:
			if verbose:
				print('Running command: %s' % cmd)
			p = Popen(cmd, **popen_kwargs)
		except Exception as e:
			print('Failed to run command: %s' % cmd)
			raise e
		else:
			break
	else:
		raise Exception('Failed to run command: %s' % commands)

	out, err = p.communicate()
	if p.returncode != 0:
		if verbose and err:

