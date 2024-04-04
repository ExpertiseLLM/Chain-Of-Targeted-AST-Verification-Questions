def _replace_register(flow_params, register_number, register_value):
	for flow_params_key, flow_params_value in flow_params.items():
		if flow_params_key == "register_value":
			flow_params[register_number] = flow_params_value
			del flow_params[flow_params_key]


