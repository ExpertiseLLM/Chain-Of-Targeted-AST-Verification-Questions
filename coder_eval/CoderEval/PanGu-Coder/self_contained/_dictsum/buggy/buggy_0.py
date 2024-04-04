def _dictsum(dicts):
    return dict(sum(d.items(), ()) for d in dicts)
