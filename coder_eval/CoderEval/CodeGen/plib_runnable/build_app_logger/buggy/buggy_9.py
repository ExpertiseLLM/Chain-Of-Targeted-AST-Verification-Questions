def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	import logging
	logging.basicConfig(filename=logfile, level=logging.INFO)
	logger = logging.getLogger(name)
	if debug:
		logger.setLevel(logging.DEBUG)
		console_handler = logging.StreamHandler()
		console_handler.setLevel(logging.INFO)
		formatter = logging.Formatter('[%(asctime)s] %(message)s')
		console_handler.setFormatter(formatter)
		logger.addHandler(console_handler)
	return logger

