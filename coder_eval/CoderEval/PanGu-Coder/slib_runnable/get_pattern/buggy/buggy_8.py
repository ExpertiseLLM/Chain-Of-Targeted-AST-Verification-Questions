def get_pattern(pattern, strip=True):
    if strip:
        pattern = re.sub(r'\s', '', pattern)
    pattern = re.sub(r'\*', '.*', pattern)
    pattern = re.sub(r'\?', '.', pattern)
    pattern = re.sub(r'\s+', '.', pattern)
    pattern = pattern.split('\n')
    pattern = [p for p in pattern if p]
    pattern = [p for p in pattern if not p.startswith('#')]
    pattern = [p.strip() for p in pattern]
    pattern = ''.join(pattern)
    return pattern
