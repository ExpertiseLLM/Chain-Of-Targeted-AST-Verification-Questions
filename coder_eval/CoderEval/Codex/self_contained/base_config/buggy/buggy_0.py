def base_config(user, etcd_host="localhost", etcd_port=2379):
	return {
		"user": user,
		"etcd_host": etcd_host,
		"etcd_port": etcd_port,
		"api_version": "v1",
		"api_base_url": "http://localhost:5000",
		"api_base_path": "/api",
		"api_static_path": "",
		"api_static_file": "",
		"api_static_file_key": "",
		"api_static_file_key_hash": "",
		"api_static_file_key_hash_algorithm": "",
		"api_static_file_key_hash_salt": "",
		"api_static_file_key_hash_iterations": 0,
		"api_static_file_key_hash_length": 0,
	}

