def _inline_r_setup(code:
	"""
	Some behaviour of R cannot be configured via env variables, but can
only be configured via R options once R has started. These are set here.
	"""
	code.inline_enabled = True
	code.inline_r_options = {"exclude": ["R"]}
	code.inline_r_options["exclude_stdlib"] = ["R"]