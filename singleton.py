class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


singleton1 = Singleton("First Instance")
print(singleton1.value)

singleton2 = Singleton("Second Instance")
print(singleton2.value)

print(singleton1 is singleton2)