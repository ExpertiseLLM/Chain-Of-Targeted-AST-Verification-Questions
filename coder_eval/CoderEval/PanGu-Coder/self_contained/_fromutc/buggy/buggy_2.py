def _fromutc(self, dt):
    return dt.astimezone(self.tzinfo)