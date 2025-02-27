API_HOSTS = {
    'test' : 'http://localhost:8880',
    'docker' : 'http://host.docker.internal:8880',
    'prod' : ''
}
API_Route = '/index.php/wp-json/wc/v3/'

WC_HOST = {
    'test': 'http://localhost:8880/index.php/',
    'docker': 'http://192.168.68.112/index.php/',
}

WC_AUTH = {
    'consumer_key': 'ck_91f178b81f4d81e447ba3ace38e99532dbfdb28b',
    'consumer_secret': 'cs_6015eba636ff57b15fc9202a7e7f356b10532149'
}

DB_HOSTS = {
    'test': 'localhost',
    'docker': 'host.docker.internal',
    'prod': ''
}

DB_PORTS = {
    'test': 8889,
    'docker': 8889,
    'prod': 0
}

DB_CREDENTIALS = {
    'user': 'root',
    'password': 'root'
}