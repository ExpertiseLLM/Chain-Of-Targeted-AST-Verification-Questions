def build_app_logger(name='app', logfile='app.log', debug=True):
    if debug:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create console handler
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s')
    ch.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(ch)
    return logger
