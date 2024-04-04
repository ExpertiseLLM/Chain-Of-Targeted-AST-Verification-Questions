def hydrate_time(nanoseconds, tz=None):
    if nanoseconds is None:
        return None
    if tz is None:
        tz = pytz.timezone('UTC')
    return tz.localize(datetime.utcfromtimestamp(nanoseconds))
