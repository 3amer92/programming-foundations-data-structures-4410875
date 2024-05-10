''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

num_students_pet = [1, 10, 12, 15, 2, 3, 5, 9 ,0 ,0 ,10]

num_of_students = len(num_students_pet)
print (num_students_pet[-1])
sum=0
for num_of_pets in num_students_pet:
  sum = sum + num_of_pets

print (sum/num_of_students)

  

