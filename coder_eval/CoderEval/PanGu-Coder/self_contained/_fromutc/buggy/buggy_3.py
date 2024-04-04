def _fromutc(self, dt):
    if dt.tzinfo is None:
        raise ValueError('Datetime object is no longer a timezone aware '
                         'datetime.')
    return dt.astimezone(self)
