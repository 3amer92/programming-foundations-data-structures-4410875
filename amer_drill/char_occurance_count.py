# Givin a string, find the number of times each character occurs


def char_occurance_count(string):
  count = {}
  for char in string:
    if char in count.keys():
      count[char] = count[char] + 1
    else:
      count[char] = 1
  return count


print (char_occurance_count("ameristhebestever"))