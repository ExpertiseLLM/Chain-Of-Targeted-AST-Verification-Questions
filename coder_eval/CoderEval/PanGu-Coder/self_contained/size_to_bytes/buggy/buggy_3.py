def size_to_bytes(size: str) -> int:
    return int(round(Decimal(size).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)))
