def remove_ending_os_sep(input_list):
    if len(input_list) > 1:
        for i in range(len(input_list) - 1):
            if input_list[i] == '\\' and input_list[i + 1]!= '/':
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = '/'
    return input_list
