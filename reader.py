def read_next(*args):
    for arg in args:
        for a in arg:
            yield a


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)