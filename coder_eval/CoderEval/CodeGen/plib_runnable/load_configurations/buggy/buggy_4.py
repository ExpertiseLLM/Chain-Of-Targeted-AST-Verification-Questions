def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. Return
the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	configurations = {}
	for filename in config_filenames:
		try:
			with open(filename, 'r') as config_file:
				config = yaml.safe_load(config_file)
		except yaml.YAMLError as e:
			print("Failed to load configuration file: " + filename + ". Exception: " + str(e))
			continue
		except IOError as e:
			print("Failed to open configuration file: " + filename + ". Exception: " + str(e))
			continue
		if not hasattr(config, 'get'):
			continue
		if not config.get('logging'):
			continue
		if not config.get('logging'):
			continue
		if 'level' in config['logging']:
			config['logging']['level'] = config['logging']['level'].upper()
		if config['logging'].get('level') and config['logging']['level'].upper() not in logging.BASIC_FORMAT:
			raise ValueError('Unknown logging level:'+ config['logging']['level'])
		if config['logging'].get('format') and config['logging']['format'].get('format') and not hasattr(logging, config['logging']['format']['format']):
			raise ValueError('Unknown logging format:'+ config['logging']['format']['format'])
		if config['logging'].get('format') and config['logging']['format'].get('format') and not hasattr(logging, config['logging']['format']['format']):
			raise ValueError('Unknown logging format:'+ config['logging']['format']['format'])
		if config['logging'].get('filename') and not config['logging'].get('filename'):
			config['logging']['filename'] = os.path.basename(filename)
		if config['logging'].get('filename'):
			if config['logging']['filename'].endswith('.log'):
				config['logging']['filename'] = config['logging']['filename'][:-4]
			else:
				config['logging']['filename'] += '.log'
		if config['components'].get('loggers'):
			loggers = config['components']['loggers']
			for logger in loggers:
				if not hasattr(logger, 'handlers'):
					logger.handlers = []
				logger.handlers.extend(config['components']['handlers']['loggers'][logger])
		if overrides:
			config['logging']['level'] = overrides.get('logging', config['logging']['level'])
			config['logging']['format'] = overrides.get('logging', config['logging']['format'])
			config['logging']['filename'] = overrides.get('logging', config['logging']['filename'])
			config['logging']['format_string'] = overrides.get('logging', config['logging']['format_string'])
		if resolve_env:
			config['logging']['level'] = resolve_level(config['logging']['level'])
			config['logging']['format'] = resolve_format(config['logging']['format'])
			config['logging']['filename'] = resolve_filename(config['logging']['filename'])
			config['logging']['format_string'] = resolve_format_string(config['logging']['format_string'])
		if config.get('components'):
			config = merge_configs(config, config['components'])
		if config.get('components'):
			config = merge_configs(config, config['components'])
		if