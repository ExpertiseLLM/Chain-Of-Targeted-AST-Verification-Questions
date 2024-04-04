def parse_frequency(frequency):
    if frequency in FREQ_TO_TIME_CONVERSION:
        return FREQ_TO_TIME_CONVERSION[frequency]
    return None
