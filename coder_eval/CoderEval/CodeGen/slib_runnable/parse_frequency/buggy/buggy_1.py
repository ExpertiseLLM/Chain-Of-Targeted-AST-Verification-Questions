def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
datetime.timedelta instance or None if the frequency is None or "always".

For instance, given "3 weeks", return datetime.timedelta(weeks=3)

Raise ValueError if the given frequency cannot be parsed.
	"""
	if frequency is None:
		return None

	if "weeks" in frequency:
		return parse_frequency(frequency.split("weeks")[0])

	if "hours" in frequency:
		return parse_frequency(frequency.split("hours")[0])

	if "days" in frequency:
		return parse_frequency(frequency.split("days")[0])

	if "months" in frequency:
		return parse_frequency(frequency.split("months")[0])

	if "years" in frequency:
		return parse_frequency(frequency.split("years")[0])

	raise ValueError("Unhandled frequency %s" % frequency)