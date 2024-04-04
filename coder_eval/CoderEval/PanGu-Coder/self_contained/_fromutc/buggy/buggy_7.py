def _fromutc(self, dt):
    if self._ambiguous(dt):
        return dt.astimezone(self._tzinfo)
    else:
        return dt