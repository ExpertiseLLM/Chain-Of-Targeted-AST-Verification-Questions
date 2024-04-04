def _inline_r_setup(code:
	"""
	Some behaviour of R cannot be configured via env variables, but can
only be configured via R options once R has started. These are set here.
	"""
	from. import _r
	_r.set_environment(env=_r.ENV.get_env())
	_r.set_options(env=_r.ENV.get_env())

