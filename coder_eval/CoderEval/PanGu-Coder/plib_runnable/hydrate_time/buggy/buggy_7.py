def hydrate_time(nanoseconds, tz=None):
    if tz is not None:
        return Time.from_nanoseconds(nanoseconds, tz)
    else:
        return Time.from_nanoseconds(nanoseconds)
