def int_to_string(number: int, alphabet: str) -> str:
    if number == 0:
        return '0'
    result = []
    while number:
        result.append(alphabet[number % len(alphabet)])
        number //= len(alphabet)
    result.reverse()
    return ''.join(result)
