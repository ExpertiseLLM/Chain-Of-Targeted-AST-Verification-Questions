def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not os.path.exists(os.path.dirname(config_filename)):
        os.makedirs(os.path.dirname(config_filename))

    with open(config_filename, 'w') as outfile:
        yaml.safe_dump(rendered_config, outfile, default_flow_style=False, encoding='utf-8', allow_unicode=True)

    if overwrite:
        os.remove(config_filename)
