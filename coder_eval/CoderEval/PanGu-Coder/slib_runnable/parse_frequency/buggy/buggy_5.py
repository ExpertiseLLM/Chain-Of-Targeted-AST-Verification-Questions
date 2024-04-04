def parse_frequency(frequency):
    if not frequency:
        return None
    if frequency in ("always", "once", "two-weeks"):
        return timedelta(weeks=1)
    try:
        return timedelta(**{freq: int(frequency) for freq in frequency.split(" ")})
    except ValueError:
        raise ValueError("Unknown frequency {0!r}".format(frequency))
