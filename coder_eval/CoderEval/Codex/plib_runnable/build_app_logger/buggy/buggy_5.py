def build_app_logger(name='app', logfile='app.log', debug=True):
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	logger.propagate = False

	# create file handler which logs even debug messages
	fh = logging.FileHandler(logfile)
	fh.setLevel(logging.DEBUG)

	# create console handler with a higher log level
	ch = logging.StreamHandler()
	if debug:
		ch.setLevel(logging.DEBUG)
	else:
		ch.setLevel(logging.INFO)

	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)
	return logger

