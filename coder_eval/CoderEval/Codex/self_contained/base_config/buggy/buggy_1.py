def base_config(user, etcd_host="localhost", etcd_port=2379):
	config = {
		"auth": {
			"type": "static",
			"users": {
				user: {
					"password": "test123"
				}
			}
		},
		"database": {
			"type": "etcd",
			"host": etcd_host,
			"port": etcd_port
		}
	}
	return config

