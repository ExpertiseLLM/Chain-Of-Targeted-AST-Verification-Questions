def _replace_register(flow_params, register_number, register_value):
    if not isinstance(flow_params, dict):
        raise ValueError("flow_params is not a dictionary")

    if register_value in flow_params:
        flow_params[register_number] = flow_params[register_value]
        del flow_params[register_value]
