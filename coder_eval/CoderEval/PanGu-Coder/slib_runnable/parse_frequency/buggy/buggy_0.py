def parse_frequency(frequency):
    try:
        return parse_frequency_string(frequency)
    except ValueError:
        return None
