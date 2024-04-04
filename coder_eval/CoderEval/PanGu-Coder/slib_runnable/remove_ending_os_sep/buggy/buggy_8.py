def remove_ending_os_sep(input_list):
    if len(input_list) <= 1:
        return input_list
    if input_list[-1] == os.sep:
        return remove_ending_os_sep(input_list[:-1])
    return input_list[:-1]
