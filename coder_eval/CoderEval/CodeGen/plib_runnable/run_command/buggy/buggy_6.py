def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	success = True
	for index, command in enumerate(commands):
		try:
			logger.info("Running command %s (input %s)", index, args)
			output = None
			env = env or os.environ
			if command[:2] == "cd" and cwd:
				if cwd == os.curdir:
					command = 'rm -rf'+ args
				else:
					command = 'cd'+ cwd +'&&'+ command[2:]
			if verbose:
				command = " ".join(shlex.quote(str(arg)) for arg in args)
			if hide_stderr:
				redirect_stderr = None
			else:
				redirect_stderr = sys.stderr
				sys.stderr = sys.stdout
			if command[:2] == "cd" and cwd:
				try:
					shutil.rmtree(cwd)
				except OSError:
					pass
				cwd = os.getcwd()
			try:
				proc = subprocess.Popen(
					command,
					cwd=cwd,
					stdin=subprocess.PIPE,
					stdout=subprocess.PIPE,
					stderr=redirect_stderr,
					env=env
				)
			except OSError:
				e = sys.exc_info()[1]
				success = False
				if e.errno == errno.ENOENT:
					logger.warning(
						"Not executing command %s: %s not found",
						args, e
					)
				else:
					logger.warning(
						"Not executing command %s: %s, %s",
						args, e.errno, e
					)
			else:
				if proc.stdin:
					proc.stdin.write(b"\n")
				proc.stdin.write(b"\x1b]1\r")
				proc.stdin.flush()
				if proc.stdout:
					proc.stdout.write(proc.stdout.read())
				proc.stdout.flush()
				if proc.stderr:
					proc.stderr.write(proc.stderr.read())
				proc.stderr.flush()
				if proc.pid:
					logger.info(
						"Successfully execute command %s", args
					)
					success = success and proc.wait() == 0
		except OSError:
			e = sys.exc_info()[1]
			if e.errno == errno.EPIPE:
				logger.warning(
					"Not executing command %s: %s",
					args, e
				)
			else:
				logger.warning(
					"Not executing command %s: %s",
					args, e
				)
	return success

