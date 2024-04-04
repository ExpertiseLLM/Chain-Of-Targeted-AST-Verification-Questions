def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if not overwrite and os.path.exists(config_filename):
		return False

	os.makedirs(os.path.dirname(config_filename), exist_ok=True)
	with open(config_filename, 'w') as f:
		f.write(rendered_config)
		os.chmod(config_filename, mode)

	return True

