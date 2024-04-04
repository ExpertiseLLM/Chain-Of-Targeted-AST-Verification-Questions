def build_app_logger(name='app', logfile='app.log', debug=True):
    
    
    log = logging.getLogger(name)
    handler = logging.FileHandler(logfile)
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
    log.addHandler(handler)
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    return log