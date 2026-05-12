# Creating a dictionary with sample data
# Dictionaries store key-value pairs, like a real dictionary but for data
student_ages = {
    "Alice": 25,
    "Bob": 22,
    "Charlie": 28,
    "Diana": 24
}

print("Original dictionary:")
print(student_ages)

# Basic operations on dictionaries:

# 1. Access a value using a key
print(f"\nAlice's age: {student_ages['Alice']}")

# 2. Add a new key-value pair
student_ages["Eve"] = 26
print(f"\nAfter adding Eve: {student_ages}")

# 3. Update an existing value
student_ages["Bob"] = 23
print(f"\nAfter updating Bob's age: {student_ages}")

# 4. Delete a key-value pair
del student_ages["Charlie"]
print(f"\nAfter deleting Charlie: {student_ages}")

# 5. Check if a key exists
if "Diana" in student_ages:
    print(f"\nDiana is in the dictionary, age: {student_ages['Diana']}")

# 6. Get all keys
print(f"\nAll keys: {list(student_ages.keys())}")

# 7. Get all values
print(f"All values: {list(student_ages.values())}")

# 8. Get all key-value pairs
print(f"All items: {list(student_ages.items())}")

# 9. Get the number of items
print(f"Number of students: {len(student_ages)}")

# 10. Iterate through the dictionary
print("\nIterating through students:")
for name, age in student_ages.items():
    print(f"{name} is {age} years old")

# 11. Clear the dictionary (remove all items)
student_ages.clear()
print(f"\nAfter clearing: {student_ages}")
