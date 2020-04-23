import configparser
import apsw
import pathlib

rewind_dir = pathlib.Path(__file__).parent.absolute()

def get_config():
    global rewind_dir
    config = configparser.ConfigParser()
    print(pathlib.PurePath(rewind_dir, 'config.ini'))
    config.read(pathlib.PurePath(rewind_dir, 'config.ini'))
    return config

def connect_db():
    config = get_config()
    return apsw.Connection(pathlib.PurePath(rewind_dir, config['DB']['db']))

def get_cursor():
    conn = connect_db()
    return conn.cursor()



