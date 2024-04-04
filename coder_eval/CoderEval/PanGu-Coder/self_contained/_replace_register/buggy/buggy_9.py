def _replace_register(flow_params, register_number, register_value):
    for key, value in flow_params.items():
        if key == register_number:
            flow_params[key] = value
