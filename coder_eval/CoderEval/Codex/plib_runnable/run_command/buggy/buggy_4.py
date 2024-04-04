def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	if not isinstance(commands, list):
		commands = [commands]

	if args is None:
		args = []

	if isinstance(args, str):
		args = [args]

	if cwd is None:
		cwd = os.getcwd()

	if cwd and not os.path.exists(cwd):
		os.makedirs(cwd)

	if env is None:
		env = os.environ

	for command in commands:
		cmd = command + " " + " ".join(args)
		print("Running:", cmd)
		if verbose:
			subprocess.check_call(cmd, cwd=cwd, env=env, shell=True)
		else:
			with open(os.devnull, "w") as fnull:
				if hide_stderr:
					stderr = fnull
				else:
					stderr = None
				subprocess
