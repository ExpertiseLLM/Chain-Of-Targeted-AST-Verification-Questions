def round_half_to_even(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(n * 2 + 1)
