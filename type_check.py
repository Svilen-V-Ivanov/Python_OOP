from functools import wraps


def type_check(variable_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for a in args:
                if type(a) != variable_type:
                    return "Bad Type"
            result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))