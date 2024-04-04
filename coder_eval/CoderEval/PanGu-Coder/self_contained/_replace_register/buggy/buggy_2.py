def _replace_register(flow_params, register_number, register_value):
    for key, flow_dict in flow_params.items():
        if key == 'flows':
            flow_params[key] = flow_dict['flows'][register_number]
        elif key == 'parameters':
            flow_params[key] = flow_dict['parameters'][register_number]
        else:
            flow_params[key] = flow_dict[register_number][key]
