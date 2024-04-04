def _dictsum(dicts):
    return _dict(reduce(operator.add, map(_dict, dicts)))
