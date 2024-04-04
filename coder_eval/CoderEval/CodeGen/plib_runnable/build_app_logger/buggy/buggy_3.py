def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	log_format = '%(asctime)s %(levelname)-8s %(message)s'
	logging.basicConfig(level=logging.DEBUG if debug else logging.INFO, format=log_format)
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	#