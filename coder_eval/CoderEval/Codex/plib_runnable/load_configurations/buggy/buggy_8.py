def load_configurations(config_filenames, overrides=None, resolve_env=True):
	# Load the configuration data.
	configs = {}
	logs = []
	for filename in config_filenames:
		config, log = load_configuration(filename, overrides, resolve_env)
		if config:
			configs[filename] = config
		if log:
			logs.append(log)
	return configs, logs


