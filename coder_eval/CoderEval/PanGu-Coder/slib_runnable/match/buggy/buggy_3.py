def match(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in SUPPORTED_TYPES