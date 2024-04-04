def parse_frequency(frequency):
    if frequency is None:
        return None
    if frequency.lower() in ("always", "never"):
        return datetime.timedelta()
    try:
        return dateutil.parser.parse(frequency)
    except ValueError:
        raise ValueError("Invalid frequency: {0}".format(frequency))
