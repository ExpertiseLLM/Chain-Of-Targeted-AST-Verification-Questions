def is_none_string(val: any) -> bool:
	if not isinstance(val, str):
		return False
	return val.lower() in ['none', 'null', 'n/a', '']


