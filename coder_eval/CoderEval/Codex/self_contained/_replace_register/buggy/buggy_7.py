def _replace_register(flow_params, register_number, register_value):
	for flow in flow_params:
		for key, value in flow['parameters'].items():
			if key == register_value:
				flow['parameters'][key] = register_number


