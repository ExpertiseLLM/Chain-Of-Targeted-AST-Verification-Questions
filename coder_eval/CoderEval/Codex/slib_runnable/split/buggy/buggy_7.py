def split(s, platform='this'):
	if platform == 'this':
		platform = (os.name == 'posix')
	
	if platform:
		# POSIX-style
		return list(re.findall(r'''((?:'[^']*'|"[^"]*"|[^'"\s]+)+)''', s))
	else:
		# Windows-style
		return list(re.findall(r'''([^'"\s]*(?:"(?:[^\\"]|\\.)*"|'(?:[^\\']|\\.)*')?[^'"\s]*)''', s))

