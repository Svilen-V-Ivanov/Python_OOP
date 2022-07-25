def fibonacci():
    first_number = 0
    second_number = 1
    yield first_number
    yield second_number

    while True:
        to_return = first_number + second_number
        first_number = second_number
        second_number = to_return
        yield to_return


generator = fibonacci()
for i in range(0):
    print(next(generator))