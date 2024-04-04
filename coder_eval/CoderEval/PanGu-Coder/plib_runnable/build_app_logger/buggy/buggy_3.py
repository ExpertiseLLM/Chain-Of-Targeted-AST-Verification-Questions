def build_app_logger(name='app', logfile='app.log', debug=True):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG if debug else logging.INFO)
    log.addHandler(logging.FileHandler(logfile))
    return log
