def _dump_string(obj, dumper=None):
    if dumper is None:
        dumper = yaml.dump
    return dumper(u'!' + _dump_object(obj))
