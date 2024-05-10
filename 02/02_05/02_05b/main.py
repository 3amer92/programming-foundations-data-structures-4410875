seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

seat_num = 0
row_num = 0
for row in seating_chart:
    row_num = row_num +1
    for seat in row:
        seat_num = seat_num +1
        student_name = seat
        print("Student name: " + student_name + " with seat number: " + str(seat_num) + " and row number: " + str(row_num) + "\n")
        