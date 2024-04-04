def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. Return
the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	config_files = []
	if overrides:
		config_files = [f for f in config_filenames if f in overrides]
	if not config_files:
		config_files = config_filenames
	else:
		config_files = config_files[:]
	if not config_files:
		raise ConfigurationError("No configuration files specified")

	logging_level = logging.WARNING
	if resolve_env:
		for f in config_files:
			logging_level = max(logging_level, get_logging_level(f, resolve_env=resolve_env))
		config_files = [f for f in config_files if get_logging_level(f, resolve_env=resolve_env) <= logging_level]

	if len(config_files) > 1:
		error_msg = "Multiple configuration files specified: %s" % config_files
		error_msg += " (see above for the location of each file)."
		raise ConfigurationError(error_msg)

	config_filename = config_files[0]
	config = read_configuration(config_filename)

	if not config:
		raise ConfigurationError("Unable to parse %s" % config_filename)
	return config, config_filename