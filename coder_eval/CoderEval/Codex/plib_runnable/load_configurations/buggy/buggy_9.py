def load_configurations(config_filenames, overrides=None, resolve_env=True):
	log_records = []
	configs = OrderedDict()
	for config_filename in config_filenames:
		try:
			configs[config_filename] = load_configuration(config_filename, overrides=overrides, resolve_env=resolve_env)
		except ConfigError as e:
			log_records.append(logging.LogRecord(
				name=__name__,
				level=logging.ERROR,
				pathname=config_filename,
				lineno=e.lineno,
				msg=e.message,
				args=(),
				exc_info=None,
				func=None,
			))
	return configs, log_records


