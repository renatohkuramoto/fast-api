import os
import configparser


def read_config_file():
    config = configparser.ConfigParser()
    root = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(root, 'config.ini')
    if os.path.isfile(config_file):
        config.read(config_file)
        return config
    return None


def get_config_db():
    config = read_config_file()
    if 'database' in config:
        return config['database']
    else:
        raise Exception('No database defined in config file')


def get_secret_key():
    config = read_config_file()
    if 'secret' in config:
        return config['secret']
    else:
        raise Exception('No secret defined in config file')
