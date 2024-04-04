def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	assert isinstance(commands, list)
	if isinstance(args, six.string_types):
		args = shlex.split(args, posix=False)
	if args and commands:
		raise ValueError('can\'t specify both args and commands')
	if args:
		if'' in args:
			raise ValueError('invalid argument: %r (max of one arg)' % args)
		env = env or os.environ
		env['LC_ALL'] = env.get('LC_ALL', 'C')
		env['LANGUAGE'] = env.get('LANGUAGE', 'C')
		env['LC_MESSAGES'] = env.get('LC_MESSAGES', 'C')

	if env is None:
		env = {}
	else:
		#