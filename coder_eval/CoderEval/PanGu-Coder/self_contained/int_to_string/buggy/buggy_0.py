def int_to_string(number: int, alphabet: List[int]) -> str:
    result = ''
    while number > 0:
        result = alphabet[number % len(alphabet)] + result
        number //= len(alphabet)
    return result
