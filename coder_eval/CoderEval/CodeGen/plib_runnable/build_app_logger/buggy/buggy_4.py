def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	
	#