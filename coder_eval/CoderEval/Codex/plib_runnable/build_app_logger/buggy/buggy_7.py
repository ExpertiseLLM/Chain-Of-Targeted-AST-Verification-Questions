def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
	logger.setLevel(logging.DEBUG)
	
	# set up console logging
	if debug:
		console = logging.StreamHandler()
		console.setLevel(logging.DEBUG)
		console.setFormatter(formatter)
		logger.addHandler(console)

	# set up file logging
	file_handler = logging.FileHandler(logfile)
	file_handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)

	return logger


