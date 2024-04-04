def base_config(user, etcd_host="localhost", etcd_port=2379):
	return {
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"authentication": {
			"enabled": True,
			"static": {
				"enabled": True,
				"users": [
					{
						"name": user,
						"password": "password"
					}
				]
			}
		},
		"logging": {
			"type": "console"
		}
	}


