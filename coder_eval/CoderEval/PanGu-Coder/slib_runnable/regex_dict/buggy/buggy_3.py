def regex_dict(item):
    return {
        key: re.compile('^' + regex + '$') for key, regex in item.items()
    }
