def base_config(user, etcd_host="localhost", etcd_port=2379):
	config = {
		"users": [
			{"user": user, "password": "pass"}
		],
		"database": {
			"host": etcd_host,
			"port": etcd_port
		},
		"key_prefix": "test",
		"secret_key": "secret",
		"auth": {
			"type": "static"
		},
		"ssl": {
			"enabled": False,
			"cert": "",
			"key": ""
		}
	}
	return config

