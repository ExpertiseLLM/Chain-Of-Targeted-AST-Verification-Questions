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
	for i in input_list:
		if len(input_list) > 1 and input_list[-1] == os.path.sep:
			input_list.pop()
		elif len(input_list) == 1 and input_list[0] == os.path.sep:
			input_list.pop(0)
		elif len(input_list) == 0:
			raise TypeError('Cannot remove a string of no paths.')
		elif len(input_list) > 1 and input_list[-1]!= os.path.sep:
			input_list.pop()
	return input_list

