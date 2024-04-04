def hydrate_time(nanoseconds, tz=None):
    if tz is None:
        tz = pytz.timezone("UTC")

    return datetime.fromtimestamp(nanoseconds / 1000, tz)
