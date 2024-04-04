def remove_ending_os_sep(input_list):
    if len(input_list) == 0:
        return input_list

    if len(input_list[0]) > 1:
        return [input_list[0]] + remove_ending_os_sep(input_list[1:])

    return input_list[0] + remove_ending_os_sep(input_list[1:])
