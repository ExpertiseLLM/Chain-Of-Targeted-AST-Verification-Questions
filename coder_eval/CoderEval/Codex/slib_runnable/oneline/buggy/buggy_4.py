def oneline(script, seperator=" && "):
	if isinstance(script, str):
		return seperator.join(script.split("\n"))
	else:
		return seperator.join(script)


