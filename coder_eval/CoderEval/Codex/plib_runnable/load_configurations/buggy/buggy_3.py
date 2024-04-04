def load_configurations(config_filenames, overrides=None, resolve_env=True):
	configurations = {}
	log_records = []
	for config_filename in config_filenames:
		try:
			configurations[config_filename] = parse_configuration(config_filename, overrides, resolve_env)
		except ConfigurationParseError as exc:
			log_records.append(exc.log_record)
		except Exception:
			log_records.append(LogRecord(logging.ERROR, "Unhandled exception while parsing configuration file {0}", config_filename))
	return configurations, log_records


