def _dictsum(dicts):
    return reduce(lambda d, k: d.update({k: d.get(k) + d.get(k)}) or d, dicts, {})
