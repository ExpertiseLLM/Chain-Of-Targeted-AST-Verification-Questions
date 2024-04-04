def _fromutc(self, dt):
    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is None:
        return dt.replace(tzinfo=None)
    else:
        return dt
