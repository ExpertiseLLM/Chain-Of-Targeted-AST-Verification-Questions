def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	assert isinstance(commands, (list, tuple))
	popen_kwargs = {
		"cwd": cwd,
		"env": env,
		"stdout": subprocess.PIPE,
		"universal_newlines": True,
	}
	if hide_stderr:
		popen_kwargs["stderr"] = subprocess.PIPE
	elif verbose:
		popen_kwargs["stderr"] = subprocess.STDOUT
	else:
		popen_kwargs["stderr"] = None
	for c in commands:
		try:
			if verbose:
				print(" ".join(c + args))
			p = subprocess.Popen(c + args, **popen_kwargs)
			output = p.communicate()[0]
			if p.returncode != 0:
				if verbose or not hide_stderr:
					# output already printed
					sys
