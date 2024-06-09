
def x_and_o(my_list):
  for i in range (len(my_list)):
    if my_list[i:3+i] == ['x','x','x']:
      return "X wins!"
    elif my_list[i:3+i] == ['o','o','o']:
      return "O wins!"
  return "No winner"



print (x_and_o(['x','x','x','o','x','o','o','o']))