def base_config(user, etcd_host="localhost", etcd_port=2379):
	config = {
		"authentication": {
			"mode": "static",
			"static": {
				"user": user
			}
		},
		"log": {
			"level": "debug",
			"file": "logs/test.log"
		},
		"database": {
			"host": etcd_host,
			"port": etcd_port
		}
	}
	return config

