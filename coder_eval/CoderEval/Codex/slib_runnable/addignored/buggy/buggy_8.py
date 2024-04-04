def addignored(ignored):
	raw = subprocess.Popen(['git', 'ls-files', '-i', '--exclude-standard'], stdout=subprocess.PIPE)
	ignored = subprocess.check_output(('grep', '-v', '^#'), stdin=raw.stdout)
	ignored = ignored.split('\n')
	ignored = [x for x in ignored if x]
	return ','.join(ignored)

