def register_vcs_handler(vcs, method):
	def register_vcs(func):
		func.vcs = vcs

		# Register on the global handler registry.
		_vcs_handlers.setdefault(vcs, []).append(func)

		return func

	return register_vcs


