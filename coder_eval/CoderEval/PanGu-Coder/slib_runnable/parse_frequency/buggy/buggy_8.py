def parse_frequency(frequency):
    if not frequency:
        return None
    frequency = frequency.strip()
    if not frequency:
        return None
    return parse_frequency_dict(frequency)
