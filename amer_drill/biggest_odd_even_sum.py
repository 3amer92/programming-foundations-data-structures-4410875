# Find the biggest odd and the biggest even in a given list and sum them.

def biggest_odd_even_sum(my_list):
  biggest_odd = my_list[0]
  biggest_even = my_list[0]
  for item in my_list:
    if item % 2 == 0 and item > biggest_even:
      biggest_even = item
    elif item % 2 != 0 and item > biggest_odd:
      biggest_odd = item      
  

  return biggest_odd + biggest_even

print(biggest_odd_even_sum([1,5,12,20,3,10,4]))