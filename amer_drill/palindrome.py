# Check if a given string is palindrome
# Palindrome: a word, phrase, or sequence that reads the same backwards as 
# forwards, e.g. madam 


def is_palindrome(string):
  left = 0
  right = len(string) - 1

  while (left < right):
    if string[left] == string[right]:
      return True
    left +=1
    right -=1
  return False


print (is_palindrome("madam"))
print (is_palindrome("amer"))