def _fromutc(self, dt):
    if dt.tzinfo is None:
        raise TypeError("Can't convert {} to a timezone-aware datetime.".format(dt))
    else:
        return dt.astimezone(self)
