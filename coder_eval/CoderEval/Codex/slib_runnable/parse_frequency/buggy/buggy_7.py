def parse_frequency(frequency):
	if frequency is None or frequency.lower() == "always":
		return None
	match = re.match(r"(\d+)\s+(\w+)", frequency)
	if not match:
		raise ValueError("Unable to parse frequency '%s'" % frequency)
	number = int(match.group(1))
	unit = match.group(2)
	if unit.lower() == "minute":
		return datetime.timedelta(minutes=number)
	elif unit.lower() == "hour":
		return datetime.timedelta(hours=number)
	elif unit.lower() == "day":
		return datetime.timedelta(days=number)
	elif unit.lower() == "week":
		return datetime.timedelta(weeks=number)
	elif unit.lower() == "month":
		return datetime.timedelta(days=30*number)
	elif unit.lower() == "year":
		return datetime.timedelta(days=365*number)
	
