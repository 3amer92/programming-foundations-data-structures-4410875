# Determine if a given list has unique characters


def has_unique_characters(my_list):
  if len(set(my_list)) == len(my_list): return True
  else: return False





print (has_unique_characters("amer"))
print (has_unique_characters("fathi"))
print (has_unique_characters("hello world"))