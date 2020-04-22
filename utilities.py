import configparser
import apsw

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def connect_db():
    config = get_config()
    return apsw.Connection(config['DB']['db'])

def get_cursor():
    conn = connect_db()
    return conn.cursor()



