def hydrate_time(nanoseconds, tz=None):
    if tz is None:
        tz = pytz.timezone(settings.TIME_ZONE)
    return datetime.datetime.fromtimestamp(nanoseconds, tz)
