def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a VCS.
	"""
	def handler(self, *args, **kwargs):
		"""
		The VCS handler.
		"""
		if vcs in self.vcs_handlers:
			raise ValueError('Cannot register duplicate VCS handler %s' % vcs)
		self.vcs_handlers[vcs] = method
		return method
	return handler

