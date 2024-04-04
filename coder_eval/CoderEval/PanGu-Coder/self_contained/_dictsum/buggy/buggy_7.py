def _dictsum(dicts):
    return reduce(operator.add, (dicts[0][k] for k in dicts[0].keys()), {})
