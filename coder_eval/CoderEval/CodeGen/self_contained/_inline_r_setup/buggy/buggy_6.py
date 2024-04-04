def _inline_r_setup(code:
	"""
	Some behaviour of R cannot be configured via env variables, but can
only be configured via R options once R has started. These are set here.
	"""
	def _get_r_executable(args: str):
		if 'R_' in args:
			r_executable = args.replace('R_', '')
			if not os.path.exists(r_executable):
				raise RuntimeError('R executable not found: %s' % r_executable)
		else:
			r_executable = 'R'
		return r_executable
	
	def _get_r_options(args: str):
		r_options = []
		if 'R_' in args:
			r_options.append('-R')
		if '--' in args:
			r_options.append('--')
	
		return r_options
	
	def _get_r_args(args: str):
		r_args = []
		if 'R_' in args:
			r_args.append('-R')
		if '--' in args:
			r_args.append('--')
		if '-R' in args:
			r_args.append('-R')
		if '-f' in args:
			r_args.append('-f')
		if '-e' in args:
			r_args.append('-e')
		if '-F' in args:
			r_args.append('-F')
		if '-p' in args:
			r_args.append('-p')
		if '-d' in args:
			r_args.append('-d')
		if '-o' in args:
			r_args.append('-o')
		if '-n' in args:
			r_args.append('-n')
		if '-L' in args:
			r_args.append('-L')
		if '-T' in args:
			r_args.append('-T')
		if '-y' in args:
			r_args.append('-y')
		if '-Y' in args:
			r_args.append('-Y')
		if '-T' in args:
			r_args.append('-T')
		if '-m' in args:
			r_args.append('-m')
		if '-M' in args:
			r_args.append('-M')
		if '-n' in args:
			r_args.append('-n')
		if '-v' in args:
			r_args.append('-v')
		if '-V' in args:
			r_args.append('-V')
		if '-z' in args:
			r_args.append('-z')
		if '--' in args:
			r_args.append('--')
		if '-S' in args:
			r_args.append('-S')
		if '-s' in args:
			r_args.append('-s')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
			r_args.append('-S')
		if '-S' in args:
