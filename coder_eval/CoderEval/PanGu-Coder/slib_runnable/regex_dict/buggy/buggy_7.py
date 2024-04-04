def regex_dict(item):
    return {k: re.compile(v) for k, v in item.items()}
