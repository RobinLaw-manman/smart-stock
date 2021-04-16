import os
import configparser


def get_config():
    try:
        PYTHON_CONFIG_PATH = os.environ['PYTHON_CONFIG_PATH']
    except Exception:
        raise ValueError
    config = configparser.ConfigParser()
    config.read(PYTHON_CONFIG_PATH)
    return config


def get_tushare_token():
    config = get_config()
    return config['TUSHARE']['TUSHARE_TOKEN']


if __name__ == '__main__':
    print(get_tushare_token())
