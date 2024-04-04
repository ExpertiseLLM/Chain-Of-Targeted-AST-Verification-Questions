def load_configurations(config_filenames, overrides=None, resolve_env=True):
	# Load and validate each configuration file.
	configurations = {}
	log_records = []
	for filename in config_filenames:
		try:
			with open(filename) as config_file:
				config = json.load(config_file)
		except (OSError, IOError, ValueError) as e:
			log_records.append(logging.LogRecord(logger.name, logging.ERROR, filename, None,
												  'Error loading configuration file: {0}'.format(e), None, None))
		else:
			# Apply any overrides to the configuration.
			if overrides:
				config = apply_overrides(config, overrides)
			# Resolve any environment variables.
			if resolve_env:
				config = resolve_environment_variables(config)
			# Validate the configuration.
			log_records.extend(validate_configuration(config,
