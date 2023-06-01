# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}{kwargs}")
        result = function(*args)
        print(f"it returned {result}")
        return result
    return wrapper
    

    

# Use the decorator 👇
@logging_decorator
def something(param0, param1, param2):
    return param0 + param1+param2

r =something(1,2,3)
print(r)