def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
datetime.timedelta instance or None if the frequency is None or "always".

For instance, given "3 weeks", return datetime.timedelta(weeks=3)

Raise ValueError if the given frequency cannot be parsed.
	"""
	freq_mapping = {
		"every": timedelta(weeks=1),
		"month": timedelta(weeks=52),
		"year": timedelta(weeks=365),
		"week": timedelta(weeks=7),
		"day": timedelta(days=1),
		"hour": timedelta(hours=1),
		"minute": timedelta(minutes=1),
		"second": timedelta(seconds=1),
		"microsecond": timedelta(microseconds=1),
		"millisecond": timedelta(milliseconds=1),
		"minute": timedelta(minutes=1),
		"hour": timedelta(hours=1),
		"day": timedelta(days=1),
		"week": timedelta(weeks=1),
		"month": timedelta(weeks=52),
		"year": timedelta(weeks=365),
		"weekday": timedelta(days=7),
		"day_of_year": timedelta(days=365),
		"weekday": timedelta(days=7),
	}
	if frequency in freq_mapping:
		return freq_mapping[frequency]
	raise ValueError("Could not parse frequency: %s" % frequency)

