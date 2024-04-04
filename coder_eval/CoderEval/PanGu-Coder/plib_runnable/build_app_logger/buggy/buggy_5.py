def build_app_logger(name='app', logfile='app.log', debug=True):
    
    
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(name)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=logfile,
                        filemode='w')
    if debug:
        logging.getLogger(name).setLevel(logging.DEBUG)
    else:
        logging.getLogger(name).setLevel(logging.INFO)