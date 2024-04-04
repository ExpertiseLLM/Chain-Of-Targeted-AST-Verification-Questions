def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)

	file_handler = logging.FileHandler(logfile)
	file_handler.setLevel(logging.DEBUG)

	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG if debug else logging.INFO)

	file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	file_handler.setFormatter(file_formatter)

	console_formatter = logging.Formatter('%(message)s')
	console_handler.setFormatter(console_formatter)

	logger.addHandler(file_handler)
	logger.addHandler(console_handler)

	return logger
