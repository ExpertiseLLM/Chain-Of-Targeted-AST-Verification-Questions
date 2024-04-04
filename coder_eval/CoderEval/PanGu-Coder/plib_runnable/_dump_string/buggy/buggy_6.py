def _dump_string(obj, dumper=None):
    return dumper.dump(obj) if dumper else str(obj)
