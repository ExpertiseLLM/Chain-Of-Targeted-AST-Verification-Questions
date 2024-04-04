def parse_frequency(frequency):
    if frequency is None:
        return None
    if frequency == "always":
        return timedelta(weeks=1)
    try:
        return timedelta(**{freq: int(frequency) for freq in FREQUENCY_LIST})
    except ValueError:
        raise ValueError("Invalid frequency: {}".format(frequency))
