def string_to_int(string: str, alphabet: str) -> int:
    return int(string, base=alphabet.index(string[0]))
