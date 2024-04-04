def get_pattern(pattern, strip=True):
    if strip:
        return re.sub(r'\s+', '\\s+', pattern)
    else:
        return re.sub(r'\s+', '\s', pattern)
