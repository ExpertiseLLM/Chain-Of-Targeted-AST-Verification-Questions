def base_config(user, etcd_host="localhost", etcd_port=2379):
	return {
		"etcd_host": etcd_host,
		"etcd_port": etcd_port,
		"authentication": {
			"static": {
				"user": user
			}
		},
		"api": {
			"port": 4000
		}
	}

