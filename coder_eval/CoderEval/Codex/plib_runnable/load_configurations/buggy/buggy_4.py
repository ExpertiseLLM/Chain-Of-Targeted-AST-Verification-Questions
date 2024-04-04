def load_configurations(config_filenames, overrides=None, resolve_env=True):
	configs = {}
	errors = []
	for config_filename in config_filenames:
		try:
			with open(config_filename, 'r') as config_file:
				config = json.load(config_file)
				if resolve_env:
					config = resolve_environment(config)
				if overrides:
					config = merge_configurations(config, overrides)
				validate_configuration(config)
				configs[config_filename] = config
		except (json.JSONDecodeError, KeyError) as err:
			errors.append(
				logging.LogRecord(
					name=__name__,
					level=logging.ERROR,
					pathname=config_filename,
					lineno=err.lineno,
					msg=err,
					args=()
				)
		
