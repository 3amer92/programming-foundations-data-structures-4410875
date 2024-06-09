# Return True if the difference between a two consicutive numbers is 1 in
# a given unsorted list, else False

def diff(my_list):

  for i in range(1, len(my_list)):
    if my_list[i] - my_list[i-1] == 1:
      return True
  return False
    

print (diff([1,1,10,2,5,7,4,6,7]))