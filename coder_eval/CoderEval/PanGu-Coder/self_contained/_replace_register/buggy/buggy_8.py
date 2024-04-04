def _replace_register(flow_params, register_number, register_value):
    for flow_param in flow_params:
        if flow_param["request_name"] == "register":
            if flow_param["register_number"] == register_number:
                flow_param["register_value"] = register_value
                break
