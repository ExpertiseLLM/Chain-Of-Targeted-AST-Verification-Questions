def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)

	# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler = logging.FileHandler(logfile)
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	return logger


