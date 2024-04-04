def _replace_register(flow_params, register_number, register_value):
    for k, v in flow_params.items():
        if v['register_number'] == register_number:
            flow_params[k]['register_value'] = register_value
            break
