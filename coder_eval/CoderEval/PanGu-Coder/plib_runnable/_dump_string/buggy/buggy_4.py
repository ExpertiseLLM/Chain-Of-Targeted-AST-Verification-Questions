def _dump_string(obj, dumper=None):
    if dumper is None:
        dumper = _UnicodeDumper()
    return dumper.dump(obj)
