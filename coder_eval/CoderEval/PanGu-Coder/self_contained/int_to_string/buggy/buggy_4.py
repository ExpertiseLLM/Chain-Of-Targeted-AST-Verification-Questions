def int_to_string(number: int, alphabet: str) -> str:
    return alphabet[number % len(alphabet)]
