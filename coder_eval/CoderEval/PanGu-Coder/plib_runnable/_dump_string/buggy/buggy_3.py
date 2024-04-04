def _dump_string(obj, dumper=None):
    if dumper is None:
        dumper = Dumper
    return dumper.represent_scalar('tag:yaml.org,2002:str', obj)
