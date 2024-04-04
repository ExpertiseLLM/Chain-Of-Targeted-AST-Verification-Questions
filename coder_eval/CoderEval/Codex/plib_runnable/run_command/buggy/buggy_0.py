def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, (list, tuple))
	popen_kwargs = {'stdout': subprocess.PIPE,
					'stderr': subprocess.PIPE,
					'cwd': cwd,
					'env': env}
	for args in commands:
		# NOTE: shell=True is required here to get the PATH searched!
		process = subprocess.Popen(args, shell=True, **popen_kwargs)
		out, err = process.communicate()
		if process.returncode != 0:
			raise Exception('Command %s failed: %s' % (args, err))
		if verbose:
			if out:
				print(out)
			if not hide_stderr and err:
				print(err)


