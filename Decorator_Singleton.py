def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    def __init__(self, value):
        self.value = value


singleton1 = Singleton("First Instance")
singleton2 = Singleton("Second Instance")
print(singleton1.value)
print(singleton1 is singleton2)