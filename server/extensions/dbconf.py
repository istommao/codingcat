from orator import DatabaseManager


config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'codingcat',
        'user': 'root',
        'password': 'smilewusheng',
        'prefix': ''
    }
}

db = DatabaseManager(config)
