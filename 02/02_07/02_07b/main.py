# Linear Search
# Search and find the item and its index
# The time complexity of the Linear Search is O(n), because we iterate only once through the list.
my_list = [6, 2, 4, 6, 8, 9, 10, 11, 20, 99, 12]


def search(list, item_to_search):
  for item in list:
    if item == item_to_search:
      return (item, list.index(item))
      
print (search (my_list, 12))
