def _replace_register(flow_params, register_number, register_value):
    for key in flow_params.keys():
        if key == "register_value":
            flow_params[key] = flow_params[key].replace(register_number, register_value)
        else:
            flow_params[key] = flow_params[key].replace(register_value, "")
