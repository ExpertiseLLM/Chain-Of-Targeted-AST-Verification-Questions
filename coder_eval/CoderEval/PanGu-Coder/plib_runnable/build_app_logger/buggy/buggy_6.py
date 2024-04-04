def build_app_logger(name='app', logfile='app.log', debug=True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    handler = logging.FileHandler(logfile)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'))
    logger.addHandler(handler)
    return logger
