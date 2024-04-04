def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG if debug else logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	# Log to file
	file_handler = logging.FileHandler(logfile)
	file_handler.setLevel(logging.DEBUG if debug else logging.INFO)
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
	# Log to console
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
	console_handler.setFormatter(formatter)
	logger.addHandler(console_handler)
	return logger

