def is_none_string(val: any) -> bool:
	return val is None or (isinstance(val, str) and val.strip().upper() == "NONE")


