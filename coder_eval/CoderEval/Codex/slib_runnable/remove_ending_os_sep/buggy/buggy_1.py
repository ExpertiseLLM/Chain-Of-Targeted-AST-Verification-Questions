def remove_ending_os_sep(input_list):
	basestring = (str, unicode)

	if not isinstance(input_list, list):
		raise TypeError("Expected list")

	result = []
	for i in input_list:
		if isinstance(i, basestring):
			if len(i) > 1 and i[-1] == os.sep:
				i = i[:-1]

		result.append(i)

	return result

