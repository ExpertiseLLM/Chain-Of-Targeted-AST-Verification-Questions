def get_pattern(pattern, strip=True):
    
    
    if strip:
        pattern = re.escape(pattern)
    return re.compile(pattern)
