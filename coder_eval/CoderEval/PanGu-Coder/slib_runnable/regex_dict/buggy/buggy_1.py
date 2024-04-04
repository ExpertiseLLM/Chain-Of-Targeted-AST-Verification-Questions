def regex_dict(item):
    return {k.replace('*.', '[.]'): v for k, v in item.items()}
