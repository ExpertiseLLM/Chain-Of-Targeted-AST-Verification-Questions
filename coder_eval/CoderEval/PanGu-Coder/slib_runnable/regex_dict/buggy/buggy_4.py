def regex_dict(item):
    return dict((k, re.compile(v)) for k, v in item.items())