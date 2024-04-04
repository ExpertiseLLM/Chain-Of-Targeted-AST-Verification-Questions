def parse_frequency(frequency):
    if frequency is None:
        return None

    # strip off any leading zeroes and parse the unit
    freq_unit, _ = parse_unit(frequency)

    if freq_unit not in FREQUENCY_UNITS:
        raise ValueError("Unknown frequency unit: %s" % freq_unit)

    return FREQUENCY_UNITS[freq_unit]
