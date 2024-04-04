def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	if isinstance(args, six.string_types):
		args = shlex.split(args, posix=True)
	if hide_stderr:
		stderr = None
	else:
		stderr = subprocess.PIPE
	logger = logging.getLogger('ansible.executor.task')
	kwargs = dict(
		cwd=cwd,
		env=env,
		verbose=verbose,
		stderr=stderr,
	)

	display.vvvv('running "%s"' % (args,), host=host)

	display.vvvv('running "%s"' % (', '.join(commands),), host=host)

	kwargs['stdout'] = PIPE
	kwargs['stderr'] = subprocess.STDOUT

	kwargs['check_rc'] = False
	p = subprocess.Popen(
		commands,
		stdout=PIPE,
		stderr=stderr,
		**kwargs
	)
	try:
		#