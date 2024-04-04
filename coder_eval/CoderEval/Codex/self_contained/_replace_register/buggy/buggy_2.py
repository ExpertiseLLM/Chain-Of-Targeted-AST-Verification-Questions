def _replace_register(flow_params, register_number, register_value):
	if not isinstance(register_value, str):
		raise ValueError("Flow parameter '{}' value must be a string".format(register_value))
	if register_value not in flow_params:
		raise ValueError("Flow parameter '{}' is not defined".format(register_value))
	flow_params[register_number] = flow_params[register_value]
	del flow_params[register_value]


