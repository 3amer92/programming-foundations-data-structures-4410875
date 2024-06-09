# Check if a given string is palindrome
# Palindrome: a word, phrase, or sequence that reads the same backwards as 
# forwards, e.g. madam 

# def is_palindrome(string):

#   left = 0
#   right = len(string) -1
#   is_pal = False

#   while (left < right):
#     print (left,right)
#     if string[left] == string[right]:
#       is_pal = True
#     else:
#       return False
#     left +=1
#     right -=1
#   return is_pal


def is_palindrome(string):
  return string == string[::-1]

print (is_palindrome("madam"))
print (is_palindrome("amer"))