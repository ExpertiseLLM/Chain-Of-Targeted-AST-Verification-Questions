def get_pattern(pattern, strip=True):
    
    
    if strip:
        return re.sub('[^A-Za-z0-9]+', '', pattern)
    else:
        return re.sub('[^A-Za-z0-9]+', '', pattern)
