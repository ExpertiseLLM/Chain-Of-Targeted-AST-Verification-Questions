def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not overwrite:
        if os.path.exists(config_filename):
            print("Configuration file already exists: %s" % config_filename)
            sys.exit(1)
    with open(config_filename, mode) as f:
        yaml.safe_dump(rendered_config, f, default_flow_style=False)
