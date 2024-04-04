def oneline(script, seperator=" && "):
	script = '\n'.join(script)
	script = script.replace('\n', seperator)
	return script

