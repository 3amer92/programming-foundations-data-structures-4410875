# X and O game, if three consicutive X's, X wins, if three consicutive O's, O wins


def x_and_o(my_list):
  x = 0
  o = 0
  for item in my_list:
    if item == 'x':
      x +=1
      o = 0
      if x == 3: return "X wins!"
    elif item == 'o':
      o +=1
      x = 0
      if o == 3: return "O wins!"
  return "No winner"

print (x_and_o(['x','x','o','x','o','o','o']))