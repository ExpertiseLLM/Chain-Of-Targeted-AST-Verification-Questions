def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. Return
the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	config_filenames = [p.rstrip('.yaml') for p in config_filenames]
	if overrides is None:
		overrides = {}
	else:
		overrides = overrides.copy()

	results = []
	log = []
	for cfg_filename in config_filenames:
		try:
			with open(cfg_filename, 'r') as cfg_file:
				cfg_file.readline()
				cfg = yaml.load(cfg_file, Loader=yaml.Loader)
				results.append(cfg)
				log.append(LogRecord(filename=cfg_filename, funcargs=cfg))
		except Exception as e:
			log.append(LogRecord(filename=cfg_filename, funcargs=None, exception=e))
			results.append({})
			print('Error reading configuration file: %s' % cfg_filename)
			print(e)
			continue
	if resolve_env:
		for result in results:
			for k, v in result.items():
				if isinstance(v, dict):
					for key, val in v.items():
						if resolve_env and isinstance(val, str):
							result[key] = resolve_env_var(val)
				elif isinstance(v, list):
					for val in v:
						if resolve_env and isinstance(val, str):
							result[val] = resolve_env_var(val)
				elif isinstance(v, dict):
					for key, val in v.items():
						if resolve_env and isinstance(val, str):
							result[key] = resolve_env_var(val)
		return results, log
	else:
		return results, log

