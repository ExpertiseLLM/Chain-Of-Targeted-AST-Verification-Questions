def parse_frequency(frequency):
	if frequency is None:
		return None
	elif frequency == "always":
		return "always"
	else:
		try:
			number, unit = frequency.split()
			number = int(number)
			unit = unit[0]
			if unit == 'd':
				return datetime.timedelta(days=number)
			elif unit == 'w':
				return datetime.timedelta(weeks=number)
			elif unit == 'm':
				return datetime.timedelta(weeks=number*4)
			elif unit == 'y':
				return datetime.timedelta(weeks=number*52)
			else:
				raise ValueError("Unable to parse frequency from '{}'".format(frequency))
		except Exception as e:
			raise ValueError("Unable to parse frequency from '{}'".format(frequency))

