def _inline_r_setup(code: str) -> str:
	# See R documentation ?options
	return code + """
	# Set options
	options(
		# Disable automatic printing of results
		# It is annoying when plotting functions get printed
		# when they are not the last statement in a block
		# It is also annoying when an R assignment is the last
		# statement in a block, and it gets printed
		# When the result is not assigned to a variable,
		# it is printed automatically by the R interpreter
		# (unless the --slave option is used),
		# so we can't disable that.
		# Note that this option is also set by the --slave option
		# when R is started.
		print.eval = FALSE,
		# Disable printing of messages
		# It is annoying when a message gets printed
		# when it is not the last statement in a block
		# When the result is not assigned to a variable,
		# it is printed automatically by the R interpreter
		# (unless the --slave option is used),
		# so we can't disable that.
		#
