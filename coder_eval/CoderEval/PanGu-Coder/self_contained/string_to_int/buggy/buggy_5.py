def string_to_int(string: str, alphabet: str = ALPHABET) -> int:
    return sum((alphabet.index(char) for char in string))
