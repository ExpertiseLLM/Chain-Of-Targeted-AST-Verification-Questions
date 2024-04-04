def is_gitbash():
	if sys.platform == 'win32':
		return os.path.basename(os.environ.get('SHELL', '')) == 'bash.exe'
	return False



