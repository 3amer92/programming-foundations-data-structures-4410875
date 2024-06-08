def has_unique_characters(data):
    # if len(set(data)) == len(data):
    #     return True
    # return False
    counter = {}
    for letter in data:
        if letter in counter.keys():
            counter[letter] = counter[letter] + 1
        else:
            counter[letter] = 0
    return counter


print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
