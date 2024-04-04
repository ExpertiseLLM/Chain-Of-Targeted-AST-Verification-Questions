def _replace_register(flow_params, register_number, register_value):
	for flow in flow_params:
		for key in flow_params[flow]:
			if key == register_value:
				flow_params[flow][key] = register_number
				break


