def string_to_int(string: str, alphabet: str) -> int:
    return int(string) - (string[-1] == '1') * (alphabet.index(string[-1]) + 1)