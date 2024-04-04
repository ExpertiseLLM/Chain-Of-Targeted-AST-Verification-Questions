def build_app_logger(name='app', logfile='app.log', debug=True):
	"""
	General purpose application logger. Useful mainly for debugging
	"""
	import logging
	from logging import Logger
	import os

	LOG = logging.getLogger(name)
	LOG.setLevel(logging.DEBUG if debug else logging.INFO)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), logfile))
	handler.setFormatter(formatter)
	LOG.addHandler(handler)

	if debug:
		handler = logging.StreamHandler()
		handler.setFormatter(formatter)
		LOG.addHandler(handler)
	else:
		LOG.setLevel(logging.INFO)

