def build_app_logger(name='app', logfile='app.log', debug=True):
	if debug:
		log_level = logging.DEBUG
	else:
		log_level = logging.INFO

	logger = logging.getLogger(name)
	logger.setLevel(log_level)

	# create file handler which logs even debug messages
	fh = logging.FileHandler(logfile)
	fh.setLevel(log_level)

	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(log_level)

	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)

	return logger


