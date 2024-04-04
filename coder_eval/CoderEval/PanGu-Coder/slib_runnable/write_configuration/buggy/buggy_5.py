def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not overwrite and os.path.isfile(config_filename):
        abort('file %s already exists' % config_filename)
    with open(config_filename, 'w') as f:
        f.write(rendered_config)
        f.flush()
        os.fsync(f.fileno())
        os.chmod(config_filename, mode)