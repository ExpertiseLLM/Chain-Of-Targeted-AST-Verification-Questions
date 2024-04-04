def base_config(user, etcd_host="localhost", etcd_port=2379):
	return {
		'etcd_host': etcd_host,
		'etcd_port': etcd_port,
		'credentials': {
			'user': user,
			'password': "test",
		},
		'network_port': 8080,
		'network_host': '0.0.0.0',
		'network_threaded': True,
		'network_debug': True,
		'network_thread_count': 16,
		'network_use_reloader': False,
		'database_name': 'test_db',
		'database_host': '0.0.0.0',
		'database_port': 27017,
		'database_user': '',
		'database_password': '',
	}

