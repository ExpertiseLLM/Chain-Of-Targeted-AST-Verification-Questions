def load_configurations(config_filenames, overrides=None, resolve_env=True):
    cfg_parser = ConfigParser()
    if resolve_env:
        cfg_parser.optionxform = str
    cfg_parser.read_file(open(config_filenames[0]))
    cfg = _load_configurations(cfg_parser, config_filenames[1:],
                               overrides=overrides)
    return cfg, cfg_parser
