# Example of a tuple in Python
my_tuple = (1, "apple", 3.14)
print(my_tuple)

f = open(r"C:\python_pratice\testfile01.txt", "r")

print(f.read())
f.close()

# Using 'with' statement to handle file operations
with open(r"C:\python_pratice\testfile01.txt", "r") as f:
    content = f.read()
    print(content)