def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	def is_flag(x):
		return (x.action is not None and
				x.action.__module__ == "argparse._flag_actions" and
				x.option_strings is not None and
				x.nargs in ("?", "*", "+", "-"))
	parser.flag_values = FlagValueDict()
	for flag in parser.flag_values.values():
		flag.value = flag.default
		flag.required = flag.required is True
		if flag.required:
			if not flag.help:
				flag.help = "(required)"
			elif not flag.metavar:
				flag.metavar = "<metavar>"
			if not flag.dest:
				flag.dest = "<dest>"
			if not flag.const:
				flag.const = "<const> (default: no constant)"
		flag.parser = parser
	for group in parser._action_groups:
		for option in group._group_actions:
			if is_flag(option):
				for flag in option._group_actions:
					if is_flag(flag):
						flag.value = flag.default
						flag.required = flag.required is True
						if flag.required:
							if not flag.help:
								flag.help = "(required)"
							elif not flag.metavar:
								flag.metavar = "<metavar>"
							if not flag.dest:
								flag.dest = "<dest>"
							if not flag.const:
								flag.const = "<const> (default: no constant)"
	return parser.flag_values