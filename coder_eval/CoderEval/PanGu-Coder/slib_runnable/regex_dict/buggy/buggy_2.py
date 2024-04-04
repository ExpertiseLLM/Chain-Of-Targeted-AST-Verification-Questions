def regex_dict(item):
    return {
        key: re.compile(key + '$') if key!= '*.h' else key
        for key in item
    }
