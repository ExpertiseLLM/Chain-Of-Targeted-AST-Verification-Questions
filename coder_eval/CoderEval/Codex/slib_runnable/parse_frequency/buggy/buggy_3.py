def parse_frequency(frequency):
	if frequency == "always" or frequency is None:
		return None
	else:
		match = FREQUENCY_RE.match(frequency)
		if match is None:
			raise ValueError("Invalid frequency: %s" % frequency)
		(number, unit) = match.groups()
		number = int(number)
		if unit == "seconds" or unit == "second":
			return datetime.timedelta(seconds=number)
		elif unit == "minutes" or unit == "minute":
			return datetime.timedelta(minutes=number)
		elif unit == "hours" or unit == "hour":
			return datetime.timedelta(hours=number)
		elif unit == "days" or unit == "day":
			return datetime.timedelta(days=number)
		elif unit == "weeks" or unit == "week":
			return datetime.timedelta(days=number * 7)
		elif unit == "months"
