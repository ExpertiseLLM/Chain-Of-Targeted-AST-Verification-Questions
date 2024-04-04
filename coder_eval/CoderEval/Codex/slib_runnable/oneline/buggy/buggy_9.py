def oneline(script, seperator=" && "):
	if isinstance(script, (list, tuple)):
		script = seperator.join(script)
	return script


