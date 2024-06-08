def find_second_smallest(my_list):
    if my_list !=[] or len(my_list) != 1:
        second_smallest = my_list[0]
        smallest = my_list[0]
        for item in my_list:
            if item < smallest:
                second_smallest = smallest
                smallest = item
        return smallest,second_smallest
    return None



print(find_second_smallest([5, 8, 3, 2, 6]))
