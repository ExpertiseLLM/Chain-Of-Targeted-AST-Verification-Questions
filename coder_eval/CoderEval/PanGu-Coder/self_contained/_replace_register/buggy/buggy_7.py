def _replace_register(flow_params, register_number, register_value):
    if register_value in flow_params['registers']:
        flow_params['registers'][register_value] = flow_params['registers'][register_value]
        del flow_params['registers'][register_value]
