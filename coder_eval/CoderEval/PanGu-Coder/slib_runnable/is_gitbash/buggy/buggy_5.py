def is_gitbash():
    return sys.platform == 'win32' and 'gitbash' in sys.executable
