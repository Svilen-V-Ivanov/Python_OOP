from collections import deque


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = deque(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        result = self.sequence.popleft()
        self.sequence.append(result)
        self.number -= 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')