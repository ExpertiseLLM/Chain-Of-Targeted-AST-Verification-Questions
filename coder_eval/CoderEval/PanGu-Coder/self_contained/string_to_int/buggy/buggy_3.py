def string_to_int(string: str, alphabet: str = string.ascii_uppercase) -> int:
    return sum(alphabet.index(c) * (26 ** idx) for idx, c in enumerate(string))
