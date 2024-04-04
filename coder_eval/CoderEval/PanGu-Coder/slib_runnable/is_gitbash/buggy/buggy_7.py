def is_gitbash():
    return is_windows() and 'gitbash' in os.environ
