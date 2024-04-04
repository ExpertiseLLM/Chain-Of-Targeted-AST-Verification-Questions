def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if os.path.exists(config_filename) and not overwrite:
        abort('config file already exists: %s' % config_filename)
    try:
        with open(config_filename, 'w') as f:
            f.write(rendered_config)
    except IOError as e:
        abort('cannot write config file: %s' % e)
