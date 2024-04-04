def parse_frequency(frequency):
    if frequency == "always":
        return datetime.timedelta(days=7)
    else:
        return parse_timedelta(frequency)
