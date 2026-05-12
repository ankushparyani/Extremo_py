# Open the file names.txt for reading in UTF-8 encoding.
# The file is automatically closed when the block ends.
with open('names.txt', 'r', encoding='utf-8') as f:
    # Read each line from the file, remove whitespace, and ignore blank lines.
    names = [line.strip() for line in f if line.strip()]
    # names = [expression for item in iterable if condition]

# Print a heading before showing the list of names.
print('Names list:')
print(type(names))
# Loop through each name in the list and print it with a dash.
for name in names:
    print('-', name)

# Print the total number of names using len().
print(f'Total names: {len(names)}')
# Print the type of the variable "names" (it should be a list).
print(f'List type: {type(names).__name__}')

# Function to count how many times each name appears and print them
def count_names(names_list):
    # Create an empty dictionary to store counts
    counts = {}
    # Loop through each name in the list
    for name in names_list:
        # If name is already in counts, add 1; else set to 1
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    
    # Directly iterate through the counts dictionary and print
    print('\nName counts:')
    for name, count in counts.items(): #for key, value in counts.items():
        print(f'{name}: {count}')

# Call the function (it handles counting and printing)
count_names(names)

