def parse_frequency(frequency):
    if frequency == "always":
        return None
    try:
        return datetime.timedelta(weeks=int(frequency))
    except ValueError:
        raise ValueError("Invalid frequency '%s'" % frequency)
