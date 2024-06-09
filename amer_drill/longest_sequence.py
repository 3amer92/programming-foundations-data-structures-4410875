# Find the longest sequence of occure in a given list of integers



def longest_sequence(my_list):
  max_seq = []
  current_seq = []

  for i in range(1, len(my_list)):
    if my_list[i] == my_list[i-1]:
        current_seq.append(my_list[i])
    else:
      if len(current_seq) > len(max_seq):
        max_seq = current_seq
      current_seq = [my_list[i]]
  if len(current_seq) > len(max_seq):
      max_seq = current_seq
  
  return max_seq

print (longest_sequence([1, 2, 2, 2, 3, 3, 2, 2, 1, 1, 1, 1]))
