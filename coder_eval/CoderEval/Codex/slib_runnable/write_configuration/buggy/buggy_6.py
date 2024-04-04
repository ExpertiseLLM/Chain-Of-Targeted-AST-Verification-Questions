def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if os.path.exists(config_filename) and not overwrite:
		raise ConfigurationError('Config file already exists: %s' % config_filename)

	parent_dir = os.path.dirname(config_filename)
	if parent_dir:
		os.makedirs(parent_dir, exist_ok=True)

	with open(config_filename, 'w') as f:
		f.write(rendered_config)
	os.chmod(config_filename, mode)


