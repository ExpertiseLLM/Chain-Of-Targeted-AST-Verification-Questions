def load_configurations(config_filenames, overrides=None, resolve_env=True):
    configs = [load_configuration(filename, overrides, resolve_env) for filename in config_filenames]
    return dict((filename, parse_configuration(config)) for filename, config in configs), configs
