def int_to_string(number: int, alphabet: str = '0123456789') -> str:
    if number < 0:
        raise ValueError('Number must be non-negative.')
    result = []
    while number > 0:
        result.append(alphabet[number % len(alphabet)])
        number //= len(alphabet)
    result.reverse()
    return ''.join(result)
