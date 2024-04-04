def _fromutc(self, dt):
    # type: (datetime.datetime) -> datetime.datetime
    if dt.tzinfo is None:
        return dt.replace(tzinfo=self._tzinfo)
    else:
        return dt.astimezone(self._tzinfo)
