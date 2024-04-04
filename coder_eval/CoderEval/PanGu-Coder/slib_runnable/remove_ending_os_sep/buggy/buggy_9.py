def remove_ending_os_sep(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        last_character = input_list[-1]
        if last_character == '/' or last_character == '\\':
            return [x for x in input_list if x!= last_character]
        else:
            return input_list[:-1]
