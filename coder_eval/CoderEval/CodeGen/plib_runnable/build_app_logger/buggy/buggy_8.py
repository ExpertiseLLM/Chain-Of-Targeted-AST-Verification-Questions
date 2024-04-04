def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	logfile = os.path.abspath(logfile)
	logging.basicConfig(
		filename=logfile,
		format='%(asctime)s %(levelname)s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S',
		level=logging.INFO,
	)
	logging.info(f'Logged to: {logfile}')
	handler = logging.FileHandler(logfile)
	handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
	if debug:
		handler.setLevel(logging.DEBUG)
	else:
		handler.setLevel(logging.INFO)
	logging.getLogger(name).addHandler(handler)
	return logging.getLogger(name)

