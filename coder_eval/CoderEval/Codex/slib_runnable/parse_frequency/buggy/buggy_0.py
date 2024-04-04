def parse_frequency(frequency):
	if frequency is None or frequency == "always":
		return None

	match = re.match(r"(\d+)\s*(\w+)", frequency)
	if match is None:
		raise ValueError("could not parse frequency '{}'".format(frequency))
	amount = int(match.group(1))
	unit = match.group(2)

	if unit == "second" or unit == "seconds":
		return datetime.timedelta(seconds=amount)
	elif unit == "minute" or unit == "minutes":
		return datetime.timedelta(minutes=amount)
	elif unit == "hour" or unit == "hours":
		return datetime.timedelta(hours=amount)
	elif unit == "day" or unit == "days":
		return datetime.timedelta(days=amount)
	elif unit == "week" or unit == "weeks":
		return datetime.timedelta(weeks=amount)
	elif unit == "month" or unit == "months":
	
