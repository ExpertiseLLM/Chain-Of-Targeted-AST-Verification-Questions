def parse_frequency(frequency):
    if frequency is None:
        return None
    elif frequency == "always":
        return datetime.timedelta(weeks=3)
    else:
        try:
            return parse_time_unit(frequency)
        except ValueError:
            raise ValueError("Frequency '{}' is not a valid time unit".format(frequency))