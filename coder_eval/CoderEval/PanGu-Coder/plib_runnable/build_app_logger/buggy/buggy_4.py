def build_app_logger(name='app', logfile='app.log', debug=True):
    if debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

    logging.getLogger(name).setLevel(log_level)

    logging.getLogger(name).addHandler(logging.StreamHandler())
    return logging.getLogger(name)