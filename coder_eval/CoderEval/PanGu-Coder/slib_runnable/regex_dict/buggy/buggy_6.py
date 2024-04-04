def regex_dict(item):
    return {k: regex_key(v) for k, v in item.items()}
