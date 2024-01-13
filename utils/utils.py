from configparser import ConfigParser


class utils:
    @staticmethod
    def read_config(env, value) -> str:
        config = ConfigParser()
        config.read('config/config.ini')
        return config.get(env, value)
