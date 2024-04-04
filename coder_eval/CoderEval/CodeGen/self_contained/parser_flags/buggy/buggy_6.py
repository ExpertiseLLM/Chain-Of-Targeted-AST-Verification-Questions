def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for flag_name, flag_value in parser.flag_values.items():
		if flag_value:
			flags += " --" + flag_name + " "
	return flags