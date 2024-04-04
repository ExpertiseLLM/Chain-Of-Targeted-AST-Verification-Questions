def regex_dict(item):
    for k, v in item.items():
        if k == '*.h' or k.endswith('.h'):
            item[k] = re.compile(v)
    return item
