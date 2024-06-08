seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

for i, row in enumerate(seating_chart):
  for j, name in enumerate(row):
    row_num = i+1
    seat_num = j +1
    print ("Student name: " + name + " : " + str(row_num) + "," + str(seat_num))
