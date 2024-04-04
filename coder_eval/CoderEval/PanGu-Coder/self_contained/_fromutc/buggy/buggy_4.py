def _fromutc(self, dt):
    # type: (datetime) -> datetime
    if dt.tzinfo is None:
        raise ValueError("Can't fromutc a naive datetime")
    return dt.astimezone(self.tz)
