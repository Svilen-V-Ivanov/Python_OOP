class dictionary_iter:
    index = 0

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def __iter__(self):
        return self

    def __next__(self):
        if dictionary_iter.index == len(self.dictionary):
            raise StopIteration
        list_of_keys = list(self.dictionary.keys())
        to_return_key = list_of_keys[dictionary_iter.index]
        to_return_value = self.dictionary[to_return_key]
        to_return_list = [to_return_key, to_return_value]
        dictionary_iter.index += 1
        return tuple(to_return_list)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)