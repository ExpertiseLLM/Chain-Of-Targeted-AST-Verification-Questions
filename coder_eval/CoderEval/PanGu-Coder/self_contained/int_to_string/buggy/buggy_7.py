def int_to_string(number: int, alphabet: str) -> str:
    return ''.join([alphabet[int(c)] for c in str(number)])
