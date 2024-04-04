def addignored(ignored):
	ignored = subprocess.check_output(['git','ls-files','-o','--exclude-standard'])
	ignored = ignored.splitlines()
	ignored = [x for x in ignored if x.startswith('.')]
	ignored = ','.join(ignored)
	return ignored

