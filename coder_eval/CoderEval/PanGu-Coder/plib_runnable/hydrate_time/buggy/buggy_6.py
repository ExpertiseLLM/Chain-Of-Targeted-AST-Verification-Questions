def hydrate_time(nanoseconds, tz=None):
    if tz is None:
        tz = get_localzone()
    return Time(nanoseconds, tz)
