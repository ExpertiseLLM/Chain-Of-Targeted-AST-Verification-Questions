def get_pattern(pattern, strip=True):
    return re.compile(pattern, flags=re.IGNORECASE if strip else 0)