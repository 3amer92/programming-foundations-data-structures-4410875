# Count of a given string occurance in files in a given directory

import os

def count_string_occurrences(directory, search_string):
    total_count = 0

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Only process files (skip directories)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                # Read the file content
                content = file.read()
                
                # Count the occurrences of the search string
                count = content.count(search_string)
                total_count += count

    return total_count

# Define the directory and search string
directory = '/workspaces/programming-foundations-data-structures-4410875/amer_drill'
search_string = 'fathi'

# Get the total count
total_count = count_string_occurrences(directory, search_string)

print(f"The string '{search_string}' occurred {total_count} times in the files in the directory '{directory}'.")
