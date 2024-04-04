def oneline(script, seperator=" && "):
	result = []
	for line in script:
		line2 = line.strip()
		if line2:
			result.append(line2)
	return seperator.join(result)
