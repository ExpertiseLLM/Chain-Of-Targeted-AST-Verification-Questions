def base_config(user, etcd_host="localhost", etcd_port=2379):
    config = {
        "etcd": {
            "host": etcd_host,
            "port": etcd_port,
            "user": user,
            "password": None,
        }
    }
    return config
