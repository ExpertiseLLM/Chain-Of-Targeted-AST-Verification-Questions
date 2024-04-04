def _fromutc(self, dt):
    return dt.replace(tzinfo=self)
