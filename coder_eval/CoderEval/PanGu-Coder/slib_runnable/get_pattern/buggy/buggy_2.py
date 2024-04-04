def get_pattern(pattern, strip=True):
    regex = re.compile(pattern)
    if strip:
        return regex.sub('', pattern)
    else:
        return regex
