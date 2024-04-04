def parse_frequency(frequency):
	if frequency is None or frequency == "always":
		return None
	if frequency == "never":
		return datetime.timedelta(weeks=52*10)
	frequency = frequency.lower()
	match = re.match(r'^\s*(\d+)\s*(\w+)\s*$', frequency)
	if match:
		number = int(match.group(1))
		unit = match.group(2)
		if unit == "day" or unit == "days":
			return datetime.timedelta(days=number)
		elif unit == "week" or unit == "weeks":
			return datetime.timedelta(weeks=number)
		elif unit == "month" or unit == "months":
			return datetime.timedelta(weeks=number*4)
		elif unit == "year" or unit == "years":
			return datetime.timedelta(weeks=number*52)
	raise ValueError("Invalid frequency: {}".format(
