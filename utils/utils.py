from configparser import ConfigParser


class utils:
    @staticmethod
    def read_config(self, env, value):
        config = ConfigParser()
        config.read('config\\config.ini')
        return config.get(env, value)
