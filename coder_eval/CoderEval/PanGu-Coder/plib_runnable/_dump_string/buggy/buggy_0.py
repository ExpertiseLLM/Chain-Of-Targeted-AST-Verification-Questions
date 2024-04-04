def _dump_string(obj, dumper=None):
    
    
    if dumper is None:
        dumper = yaml.SafeDumper

    return dumper.represent_scalar('tag:yaml.org,2002:str', str(obj))
