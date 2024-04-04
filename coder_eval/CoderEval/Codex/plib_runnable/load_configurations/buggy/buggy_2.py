def load_configurations(config_filenames, overrides=None, resolve_env=True):
	if overrides is None:
		overrides = {}
	validator = ConfigValidator(overrides)
	errs = []
	configs = {}
	for filename in config_filenames:
		try:
			with open(filename) as f:
				configs[filename] = validator.validate(json.load(f), resolve_env=resolve_env)
		except IOError as e:
			errs.append(logging.LogRecord(
				name="config",
				level=logging.ERROR,
				pathname=filename,
				msg="Unable to load configuration file: %s" % e,
			))
		except ValueError as e:
			errs.append(logging.LogRecord(
				name="config",
				level=logging.ERROR,
				pathname=filename,
				msg="Unable to parse configuration file: %s" % e,
	
