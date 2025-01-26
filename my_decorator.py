def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()




def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returner {result}")
        return result
    return wrapper

@log_execution
def add(a, b):
    return a + b
result = add(5, 3)