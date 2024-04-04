def _replace_register(flow_params, register_number, register_value):
	"""
	Replace value from flows to given register number

'register_value' key in dictionary will be replaced by register number
given by'register_number'

:param flow_params: Dictionary containing defined flows
:param register_number: The number of register where value will be stored
:param register_value: Key to be replaced by register number
	"""
	for flow_id in flow_params:
		if flow_params[flow_id]['type'] == 'flow':
			flow_id_list = flow_params[flow_id]['flow_ids']
			if register_number in flow_id_list:
				flow_params[flow_id]['value'] = register_value

