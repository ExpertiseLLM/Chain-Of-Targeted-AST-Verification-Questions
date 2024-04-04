def base_config(user, etcd_host="localhost", etcd_port=2379):
	config = {}
	config["auth"] = {
		"static": {
			"user": user,
			"password": "password"
		}
	}
	config["db"] = {
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		}
	}
	return config


