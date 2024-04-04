def base_config(user, etcd_host="localhost", etcd_port=2379):
	return {
		"user": user,
		"etcd_host": etcd_host,
		"etcd_port": etcd_port,
		"etcd_ca": "",
		"etcd_cert": "",
		"etcd_key": "",
		"etcd_user": "",
		"etcd_password": ""
	}


