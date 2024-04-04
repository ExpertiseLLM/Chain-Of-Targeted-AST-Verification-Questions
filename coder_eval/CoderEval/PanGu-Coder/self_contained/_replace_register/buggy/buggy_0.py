def _replace_register(flow_params, register_number, register_value):
    for k, v in flow_params.items():
        if k == "flows":
            flow_params[k][register_number] = v
        elif k == "register_value":
            flow_params[k][register_number] = register_value
