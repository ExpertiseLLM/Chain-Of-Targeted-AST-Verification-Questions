def load_configurations(config_filenames, overrides=None, resolve_env=True):
	if overrides is None:
		overrides = {}
	if resolve_env:
		overrides = resolve_environment_overrides(overrides)
	return load_configurations_from_dict(dict(zip(config_filenames, map(json.load, config_filenames))), overrides)


