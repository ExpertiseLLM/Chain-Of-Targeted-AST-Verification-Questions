def int_to_string(number: int, alphabet: str) -> str:
    if number < 0:
        raise ValueError("Input value must be non-negative")
    return alphabet[number]
