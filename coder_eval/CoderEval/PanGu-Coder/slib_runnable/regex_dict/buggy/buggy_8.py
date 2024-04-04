def regex_dict(item):
    return {k: re.sub(r'\.(\w+)$', r'\1.', v) for k, v in item.items()}
