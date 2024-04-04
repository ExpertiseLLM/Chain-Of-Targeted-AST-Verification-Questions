def register_vcs_handler(vcs, method):
	
	def wrapper(func):
		
		if not hasattr(func, 'vcs_handlers'):
			func.vcs_handlers = list()
		
		func.vcs_handlers.append((vcs, method))
		
		return func
	
	return wrapper


