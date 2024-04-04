def hydrate_time(nanoseconds, tz=None):
    if not tz:
        tz = timezone.get_current_timezone()
    return datetime.time(nanoseconds=nanoseconds, tzinfo=tz)
