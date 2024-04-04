def _dictsum(dicts):
    return dict(sum(((dict((d.items() if hasattr(d, 'items') else d)) if hasattr(d, 'items') else d),) if hasattr(d, 'items') else () for d in dicts),)
