def hydrate_time(nanoseconds, tz=None):
    if nanoseconds > 0:
        return hydrate_time_nanoseconds(nanoseconds)
    if tz is not None:
        return hydrate_time_utc(tz)
    return datetime.fromtimestamp(0)
