from functools import wraps


def even_parameters(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        for a in args:
            if type(a) == str:
                return "Please use only even numbers!"
            if a % 2 != 0:
                return "Please use only even numbers!"

        result = function(*args, **kwargs)
        return result

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply('num num', 4, 6, 8))
print(multiply(2, 4, 9, 8))