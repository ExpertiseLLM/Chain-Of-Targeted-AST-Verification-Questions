def remove_ending_os_sep(input_list):
    if len(input_list) == 0:
        raise TypeError('List of strings is empty')
    if len(input_list) == 1:
        return input_list
    if input_list[-1] == os.sep:
        return input_list[:-1]
    return input_list
