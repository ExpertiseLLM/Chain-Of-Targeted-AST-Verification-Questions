def parse_frequency(frequency):
	if frequency is None or frequency == "always":
		return None

	frequency_re = re.compile(r"^(\d+) *(\w+)$")
	match = frequency_re.match(frequency)
	if match is None:
		raise ValueError(f"Could not parse frequency: {frequency}")

	num, unit = match.groups()
	num = int(num)

	if unit.startswith("min"):
		return datetime.timedelta(minutes=num)
	elif unit.startswith("hour"):
		return datetime.timedelta(hours=num)
	elif unit.startswith("day"):
		return datetime.timedelta(days=num)
	elif unit.startswith("week"):
		return datetime.timedelta(weeks=num)
	elif unit.startswith("month"):
		return datetime.timedelta(weeks=4 * num)
	elif unit.startswith("year"):
		return datetime
