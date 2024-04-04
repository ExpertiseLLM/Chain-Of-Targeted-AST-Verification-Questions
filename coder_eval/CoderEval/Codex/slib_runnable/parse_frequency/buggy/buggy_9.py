def parse_frequency(frequency):
	if frequency is None or frequency == "always":
		return None

	frequency = frequency.strip()
	match = FREQUENCY_PATTERN.match(frequency)
	if match is None:
		raise ValueError("Cannot parse frequency %r" % frequency)

	number, unit = match.groups()
	number = int(number)

	if unit in ("minutes", "min"):
		return datetime.timedelta(minutes=number)
	elif unit in ("hours", "hour"):
		return datetime.timedelta(hours=number)
	elif unit in ("days", "day"):
		return datetime.timedelta(days=number)
	elif unit in ("weeks", "week"):
		return datetime.timedelta(weeks=number)
	elif unit in ("months", "month"):
		return datetime.timedelta(days=number*30)
	elif unit in ("years", "year"):
		return datetime.timedelta(days=number*365)
