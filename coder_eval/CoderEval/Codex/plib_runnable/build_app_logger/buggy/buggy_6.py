def build_app_logger(name='app', logfile='app.log', debug=True):
	# TODO: Check we are logging to file and stderr
	l = logging.getLogger(name)
	l.setLevel(logging.DEBUG)

	# Create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	# Create file handler and set level to debug
	fh = logging.FileHandler(logfile, mode='a')
	fh.setLevel(logging.DEBUG)

	# Create formatter
	formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s',
								  datefmt='%Y-%m-%d %H:%M:%S')

	# Add formatter to ch
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)

	# Add ch and fh to logger
	l.addHandler(ch)
	l.addHandler(fh)
	return l

