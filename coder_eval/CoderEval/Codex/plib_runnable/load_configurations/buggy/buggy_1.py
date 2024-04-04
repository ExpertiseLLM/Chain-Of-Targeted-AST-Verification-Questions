def load_configurations(config_filenames, overrides=None, resolve_env=True):
	configurations = {}
	errors = []
	for config_filename in config_filenames:
		config_filename = os.path.abspath(config_filename)
		try:
			with open(config_filename, encoding='utf-8') as config_file:
				config_data = config_file.read()
		except OSError as e:
			record = logging.LogRecord(__name__, logging.ERROR, config_filename, 0, 'unable to read configuration file "{filename}": {error}', (), None, 'load_configurations')
			record.filename = config_filename
			record.error = e
			errors.append(record)
			continue
		try:
			configuration = json.loads(config_data)
		except UnicodeError as e:
			record = logging.LogRecord(__name__, logging.ERROR, config_filename, 0, 'unable to decode configuration file "{filename}": {error}', (), None, 'load_configurations')
