def base_config(user, etcd_host="localhost", etcd_port=2379):
	return {
		'etcd_host': etcd_host,
		'etcd_port': etcd_port,
		'auth': {
			'static': {
				'user': user,
				'password': 'secret'
			}
		}
	}


