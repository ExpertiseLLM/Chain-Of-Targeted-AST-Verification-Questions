def split(s, platform='this'):
	return re.findall(shlex.shlex(s, posix=platform!=0))

