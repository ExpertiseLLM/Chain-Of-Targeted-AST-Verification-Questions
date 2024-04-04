def parse_version(s: str) -> str:
    
    
    return '.'.join(map(str, map(int, s.split('.'))))
