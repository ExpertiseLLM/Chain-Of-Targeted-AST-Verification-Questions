def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):

    if not os.path.exists(os.path.dirname(config_filename)):
        os.makedirs(os.path.dirname(config_filename))
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file, default_flow_style=False, explicit_start=True, explicit_end=True, width=mode, Dumper=Dumper, line_length=80, allow_unicode=True, encoding='utf-8', allow_system_config_changes=False)
