# Given two lists, return true if the second list is anagram of the first one.
# An Anagram is a word or phrase formed by rearrangir the letters of a 
# different word or phrase, typically using all the original letters exactly once.


def valid_anagram(first_list, second_list):
  if set(second_list).intersection(set(first_list)) == set(first_list):
    return True
  else:
    return False


print (valid_anagram("amer","rmea"))
print (valid_anagram("amer","ali"))