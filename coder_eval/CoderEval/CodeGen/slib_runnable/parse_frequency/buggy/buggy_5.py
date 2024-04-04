def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
datetime.timedelta instance or None if the frequency is None or "always".

For instance, given "3 weeks", return datetime.timedelta(weeks=3)

Raise ValueError if the given frequency cannot be parsed.
	"""
	time_unit = frequency.split(" ")[1]
	try:
		frequency = int(frequency)
	except ValueError:
		if time_unit == "Y":
			frequency = 0
		elif time_unit == "M":
			frequency = 12
		elif time_unit == "D":
			frequency = 24
		elif time_unit == "H":
			frequency = 3600
		elif time_unit == "S":
			frequency = 3600 * 24
		else:
			raise ValueError("Invalid frequency unit")
	return datetime.timedelta(weeks=frequency, minutes=frequency * 60, seconds=frequency * 60 * 60)

