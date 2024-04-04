def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	console.setFormatter(formatter)
	logger.addHandler(console)
	if debug:
		logger.info('Logger created in debug mode')
	else:
		logger.info('Logger created in release mode')
	return logger

