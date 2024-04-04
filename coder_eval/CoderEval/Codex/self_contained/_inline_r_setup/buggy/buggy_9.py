def _inline_r_setup(code: str) -> str:
	if '--no-save' in R_OPTIONS:
		# --no-save is required for speed, but it makes R print a warning
		# every time it is used, we don't want to see that
		code = "options(warn=-1);" + code
	return code


