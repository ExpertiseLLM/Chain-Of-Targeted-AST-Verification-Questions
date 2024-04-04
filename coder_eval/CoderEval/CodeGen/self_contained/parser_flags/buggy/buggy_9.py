def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	if parser.required:
		flags += "-r"
	if parser.add_help:
		flags += "-h"

	if parser.formatter_class is not None:
		flags += "-f"
	if parser.prefix_chars:
		flags += "-P" + parser.prefix_chars

	if parser.argument_class is not None:
		flags += "-A"

	if parser.no_value:
		flags += "-N"

	if parser.no_log:
		flags += "-L"

	if parser.hidden:
		flags += "-i"

	if parser.help:
		flags += parser.help

	if parser.name:
		flags += "-n" + parser.name

	if parser.version:
		flags += "-V" + parser.version

	if parser.src:
		flags += "-S" + parser.src

	if parser.strict:
		flags += "-s"

	if parser.treat_as_stdout:
		flags += "-T"

	if parser.verbose:
		flags += "-v"

	if parser.verbose2:
		flags += "-v2"

	if parser.quiet:
		flags += "-q"

	if parser.multiline:
		flags += "-m"

	if parser.version_file:
		flags += "-V" + parser.version_file

	if parser.version_flag:
		flags += "-V" + parser.version_flag

	if parser.version_header:
		flags += "-V" + parser.version_header

	if parser.version_source_code:
		flags += "-V" + parser.version_source_code

	if parser.version_info:
		flags += "-V" + parser.version_info

	if parser.version_link:
		flags += "-V" + parser.version_link

	if parser.version_url:
		flags += "-V" + parser.version_url

	if parser.version_branch:
		flags += "-V" + parser.version_branch

	if parser.version_branch_option:
		flags += "-V" + parser.version_branch_option

	if parser.version_branch_commit:
		flags += "-V" + parser.version_branch_commit

	if parser.version_branch_tag:
		flags += "-V" + parser.version_branch_tag

	if parser.version_branch_date:
		flags += "-V" + parser.version_branch_date

	if parser.version_branch_date_option:
		flags += "-V" + parser.version_branch_date_option

	if parser.version_branch_date_time:
		flags += "-V" + parser.version_branch_date_time

	if parser.version_branch_date_time_option:
		flags += "-V" + parser.version_branch_date_time_option

	if parser.version_branch_date_number:
		flags += "-V" + parser.version_branch_date_number

	if parser.version_branch_date_number_option:
		flags += "-V" + parser.version_branch_date_number_option

	if parser.version_branch_line_break:
		flags += "-V" + parser.version_branch_line_break

	if parser.version_branch_line_break_option:
		flags += "-V" + parser.version_branch_line_break_option

	if parser.version_branch_line_end:
		flags += "-V" + parser.version_branch_line_end

	if parser.version_branch_line_end_option:
		flags += "-V" + parser.version_branch_line_end_option

	if parser.version_branch_line_start:
		flags += "-V" + parser.version_branch_line_start

	if parser.version_branch_line_start_option:
		flags += "-V" + parser.version_branch_line_start_option

	if parser.version_branch_line