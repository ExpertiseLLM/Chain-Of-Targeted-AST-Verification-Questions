def hydrate_time(nanoseconds, tz=None):
    if tz is None:
        tz = pytz.timezone('Europe/London')
    return datetime.time(
        hour=nanoseconds // 10000,
        minute=nanoseconds % 10000,
        second=nanoseconds % 100,
        tzinfo=tz
    )
