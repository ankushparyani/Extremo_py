phonebook = {
    'Alice': '555-1234',
    'Bob': '555-5678',
    'Charlie': '555-9012'
}

# Add a new entry
phonebook['Diana'] = '555-3456'

#another ways to add a new entry 
phonebook.update({'Alice': '555-0000'})

# Look up a number
print(phonebook['Bob'])  # prints 555-5678

#another way to look up a number
print(phonebook.get('Charlie'))  # prints 555-9012

# Check if a name is in the phonebook
if 'Alice' in phonebook:
    print('Alice is in the phonebook.')

#delete an entry
del phonebook['Diana']

print(phonebook)

# Iterate through entries
for name, number in phonebook.items():
    print(f'{name}: {number}')
