def addignored(ignored):
	ignored = subprocess.check_output(['git', 'ls-files', '-i', '-o', '--exclude-standard']).splitlines()
	ignored.sort()
	return ", ".join(ignored)


