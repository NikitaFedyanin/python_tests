class Singleton:
    instance = None
    is_init = False

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not self.is_init:
            self.count = 5
            self.is_init = True


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    def write_log(self, path):
        pass


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2
pass
