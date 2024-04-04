def parse_frequency(frequency):
	if frequency is None:
		return None
	if frequency == "always":
		return None
	number, unit = frequency.split(" ")
	number = int(number)
	if unit == "minutes":
		return datetime.timedelta(minutes=number)
	elif unit == "hours":
		return datetime.timedelta(hours=number)
	elif unit == "days":
		return datetime.timedelta(days=number)
	elif unit == "weeks":
		return datetime.timedelta(weeks=number)
	else:
		raise ValueError("invalid unit: %s" % unit)

