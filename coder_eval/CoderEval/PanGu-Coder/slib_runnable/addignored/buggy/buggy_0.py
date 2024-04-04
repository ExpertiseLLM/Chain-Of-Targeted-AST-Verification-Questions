def addignored(ignored):
    ignored = ignored.split(',')
    ignored = [f for f in ignored if not f.startswith('.')]
    ignored.sort()
    return ','.join(ignored)
