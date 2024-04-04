def remove_ending_os_sep(input_list):
    if len(input_list) <= 1:
        return input_list

    return [remove_ending_os_sep(item) for item in input_list]
