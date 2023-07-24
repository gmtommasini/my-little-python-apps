import time
import functools

# Note: Here, the _function argument acts as a marker, noting whether 
# the decorator has been called with arguments or not:
def performance_measurer(_function=None, *, print_args=None):
    """
    A decorator function for measuring the execution time of a given function.

    Usage:
    @performance_measurer(print_args=True)
    def my_function(arg1, arg2, ...):
        # Function body

    Parameters:
    print_args (bool, optional): If True, the decorator will print the function name, arguments, and keyword arguments
                                 when the function is called. If False, only the function name will be printed.
                                 Default is None, which means it will print the function name without arguments.

    """
    def decorator_function(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if print_args:
                print(f"You called {function.__name__}{args}{kwargs}")
            else:
                print(f"You called {function.__name__}")
            start = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            total = end - start
            print(f"Function '{function.__name__}' took {total:.6f} seconds to execute.")
            return result
        return wrapper
    return decorator_function(_function) if _function else decorator_function


if __name__ == '__main__':
    pass

