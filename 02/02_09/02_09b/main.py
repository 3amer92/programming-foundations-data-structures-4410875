# Find the second smalles number
# We could have used the "sorted" built-in function and simply get the value of index [1]
# but its time complexity is O(n log n), so it is not worth.
# The time complexity of the below code is O(n) because we iterate only once.

def find_second_smallest(my_list):
    if len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        smallest = my_list[0]
        second_smallest = my_list[0]
        for item in my_list:
            if item < smallest:
                second_smallest = smallest
                smallest = item
            elif item < second_smallest:
                second_smallest = item
        return (smallest, second_smallest)
            
            


print(find_second_smallest([5, 8, 3, 2, 6]))
