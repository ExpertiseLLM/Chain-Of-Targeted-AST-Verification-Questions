def parse_frequency(frequency):
	if frequency == "always":
		return None

	if frequency is None:
		return None

	if frequency == "weekly":
		return datetime.timedelta(weeks=1)

	if frequency == "daily":
		return datetime.timedelta(days=1)

	if frequency == "monthly":
		return datetime.timedelta(weeks=4)

	if frequency == "yearly":
		return datetime.timedelta(weeks=52)

	raise ValueError(f"Unknown frequency: {frequency}")


