def hydrate_time(nanoseconds, tz=None):
    if nanoseconds < 0:
        return None

    if tz is None:
        tz = get_local_timezone()

    if isinstance(tz, str):
        tz = pytz.timezone(tz)

    return tz.localize(datetime.fromtimestamp(nanoseconds))
