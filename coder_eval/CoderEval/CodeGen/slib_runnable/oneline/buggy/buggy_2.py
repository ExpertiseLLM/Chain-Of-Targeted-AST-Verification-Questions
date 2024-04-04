def oneline(script, seperator=" && "):
	"""
	converts a script to one line command.
THis is useful to run a single ssh command and pass a one line script.

:param script:
:return:
	"""
	lines = script.split(seperator)
	return script.format(*lines)