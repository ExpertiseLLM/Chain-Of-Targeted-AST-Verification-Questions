def oneline(script, seperator=" && "):
	"""
	converts a script to one line command.
THis is useful to run a single ssh command and pass a one line script.

:param script:
:return:
	"""
	if script == None:
		return
	if script == '':
		return ''
	return script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator +'&&'+ script +'&&'+ seperator

