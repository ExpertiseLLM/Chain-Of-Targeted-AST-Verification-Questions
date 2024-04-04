def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	import logging
	import logging.handlers
	from logging.handlers import RotatingFileHandler
	from logging import Formatter
	import os

	logger = logging.getLogger(name)

	if not debug:
		logger.setLevel(logging.WARNING)
	else:
		logger.setLevel(logging.INFO)
		logger.propagate = False

	formatter = Formatter(
		'%(asctime)s - %(levelname)s - %(message)s'
	)

	app_logger = RotatingFileHandler(
		filename=logfile,
		mode='a',
		maxBytes=10**6,
		backupCount=5
	)

	app_logger.setFormatter(formatter)
	app_logger.setLevel(logging.DEBUG)
	logger.addHandler(app_logger)

	if os.environ.get('ENV')!= 'production':
		logger.addHandler(StreamHandler(sys.stdout))