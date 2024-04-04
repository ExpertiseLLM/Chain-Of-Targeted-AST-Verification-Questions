def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if config_filename.endswith('/'):
		raise ValueError('config_filename should be a file, not a directory')

	if os.path.exists(config_filename) and not overwrite:
		raise ValueError('Config file already exists: {}'.format(config_filename))

	# Ensure the parent directory exists
	parent_dir = os.path.dirname(config_filename)
	if not os.path.exists(parent_dir):
		os.makedirs(parent_dir)

	# Write the file
	with open(config_filename, 'w') as fh:
		fh.write(rendered_config)

	os.chmod(config_filename, mode)


