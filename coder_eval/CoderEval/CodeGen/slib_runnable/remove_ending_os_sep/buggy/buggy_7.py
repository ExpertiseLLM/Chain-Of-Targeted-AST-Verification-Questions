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
	if type(input_list) is not list:
		raise TypeError("input_list must be of type list")
	if len(input_list) == 0:
		return []
	if len(input_list) > 1:
		for i in range(len(input_list) - 1):
			if input_list[i] == os.path.sep:
				input_list[i] = ""
	else:
		if input_list[0] == os.path.sep:
			input_list = input_list[1:]
	return input_list