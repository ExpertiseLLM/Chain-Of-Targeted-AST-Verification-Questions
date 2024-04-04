def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    with open(config_filename, mode) as f:
        f.write(rendered_config)
