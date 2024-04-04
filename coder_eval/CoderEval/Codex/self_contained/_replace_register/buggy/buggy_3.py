def _replace_register(flow_params, register_number, register_value):
	for flow in flow_params:
		if isinstance(flow_params[flow], dict):
			_replace_register(flow_params[flow], register_number, register_value)
		elif flow_params[flow] == register_value:
			flow_params[flow] = register_number

