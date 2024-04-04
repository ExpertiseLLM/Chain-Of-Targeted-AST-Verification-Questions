def load_configurations(config_filenames, overrides=None, resolve_env=True):
	configs = {}
	config_errors = []
	for config_filename in config_filenames:
		try:
			config = load_configuration(config_filename, overrides=overrides, resolve_env=resolve_env)
			configs[config_filename] = config
		except ValidationError as e:
			config_errors.append(logging.LogRecord(
				name=__name__,
				level=logging.ERROR,
				pathname=config_filename,
				lineno=e.errors[0].line_number,
				msg=str(e),
				args=(),
				exc_info=None
			))
	return configs, config_errors


