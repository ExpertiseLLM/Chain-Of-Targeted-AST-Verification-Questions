def _c_optimizations_required():
	#
	# First, check if the user has explicitly requested the use of the C
	# optimizations.
	#
	if 'PURE_PYTHON' in os.environ:
		#
		# The user has specified an environment variable. Simply return its
		# value.
		#
		return not os.environ['PURE_PYTHON']
	#
	# Now, check if the current Python interpreter is running in a virtual
	# environment.
	#
	if hasattr(sys, 'real_prefix'):
		#
		# The Python interpreter is running in a virtual environment.
		#
		# Now, check if the virtual environment is a virtualenv.
		#
		if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
			#
			# The virtual environment is a virtualenv.
			#
			# Note: because of the way virtualenv works, this cannot be the
			# system Python interpreter.
			#

