# Given two lists (string and sub-string), you need to find the number
# of times the sub-string occurs in the string.


def find_string(string, substring):
  count = 0
  for i in range(len(string) - len(substring) +1):
    if string[i:len(substring)+i] == substring:
      count +=1
  return count




print (find_string("ABCDCDC", "CDC"))
