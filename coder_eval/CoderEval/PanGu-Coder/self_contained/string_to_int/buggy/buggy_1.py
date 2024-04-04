def string_to_int(string: str, alphabet: str = ALPHABET) -> int:
    return int(''.join([alphabet[i] for i in string]))
