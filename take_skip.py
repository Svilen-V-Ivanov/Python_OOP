class take_skip:
    counter = 1

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if take_skip.counter > self.count:
            raise StopIteration
        value_to_append = 0 + self.step * (take_skip.counter - 1)
        take_skip.counter += 1
        return value_to_append


numbers = take_skip(10, 5)
for number in numbers:
    print(number)