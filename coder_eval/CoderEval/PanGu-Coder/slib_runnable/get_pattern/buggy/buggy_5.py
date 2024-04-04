def get_pattern(pattern, strip=True):
    
    
    if not isinstance(pattern, str):
        raise TypeError('The given pattern must be a string')
    return re.compile(pattern, re.IGNORECASE if strip else 0)
