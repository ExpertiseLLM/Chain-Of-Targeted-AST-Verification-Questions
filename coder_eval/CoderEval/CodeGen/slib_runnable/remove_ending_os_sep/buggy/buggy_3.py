def remove_ending_os_sep(input_list):
	"""
	Iterate over a string list and remove trailing os seperator characters.

Each string is tested if its length is greater than one and if the last
character is the pathname seperator. If so, the pathname seperator character
is removed.

Args:
    input_list: list of strings

Returns:
    Processed list of strings

Raises:
    TypeError
	"""
	#