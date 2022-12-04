import configparser
from pathlib import Path

CONFIG_DATA_DIR = f'{Path(__file__).parent.parent.resolve()}/Configurations/'
config = configparser.RawConfigParser()
config.read(f'{CONFIG_DATA_DIR}config.ini')


class ReadConfig():
    @staticmethod
    def api_base_url():
        return config.get('common', 'baseURL')

    @staticmethod
    def api_end_point():
        return config.get('common', 'endPoint')

    @staticmethod
    def api_params():
        return config.get('common', 'params')


if __name__ == '__main__':
    print(ReadConfig().api_base_url())
