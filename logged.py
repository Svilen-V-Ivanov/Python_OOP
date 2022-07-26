from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = f"you called {function.__name__}{args}\n"
        func_value = function(*args, **kwargs)
        return result + f"it returned {func_value}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))