def parser_flags(parser):
	flags = parser.format_usage()
	flags = re.sub(r"^usage:", "", flags, flags=re.IGNORECASE)
	flags = re.sub(r"\[.*\]", "", flags)
	flags = re.sub(r"  +", " ", flags)
	flags = re.sub(r"^\s+|\s+$", "", flags)
	return flags

