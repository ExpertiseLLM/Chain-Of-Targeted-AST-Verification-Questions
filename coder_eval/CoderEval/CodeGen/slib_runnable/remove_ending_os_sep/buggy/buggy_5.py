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
	if type(input_list) not in [str, list]:
		raise TypeError("Input list must be of type list")
	if type(input_list) is str:
		pass
	elif type(input_list) is list:
		for i in range(len(input_list)):
			if type(input_list[i]) is str:
				if len(input_list[i]) > 1:
					input_list[i] = input_list[i][1:]
	else:
		raise TypeError("Input list must be of type list")
	return input_list