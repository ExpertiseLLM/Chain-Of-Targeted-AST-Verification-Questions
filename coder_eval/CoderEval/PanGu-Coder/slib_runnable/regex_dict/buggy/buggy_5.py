def regex_dict(item):
    return {re.sub('\.cpp$', '.regex', key): value for key, value in item.items()}
