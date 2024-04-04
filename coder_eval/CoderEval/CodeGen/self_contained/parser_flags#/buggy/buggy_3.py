def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ''
	for flag_name in parser.flag_names:
		flag_value = parser.flag_values.get(flag_name, None)
		if flag_value is not None:
			flag_value = str(flag_value).replace('\n','')
			if flag_value.startswith('-'):
				flag_value = flag_value[1:]
			flags += flag_name + '=' + flag_value +''
	return flags.strip()

