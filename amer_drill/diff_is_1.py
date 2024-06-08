# Return True if the difference between a two consicutive numbers is 1 in
# a given unsorted list, else False

def diff(my_list):
  index = 0
  for item in my_list:
    index += 1
    if index == len(my_list): # To not exceed the range
      return False
    next_item = my_list[index]
    if item - next_item == 1:
      return True
    

print (diff([1,1,10,2,5,6,4,6,5]))