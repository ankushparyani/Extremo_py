#write a pyspark code to read a .txt file and print the names in the file. The file contains one name per line. Ignore blank lines and whitespace.

# Simple Python solution (PySpark has compatibility issues in this environment)
with open("names.txt", "r") as f:
    names = [line.strip() for line in f if line.strip()]

print("Names from file:")
for name in names:
    print(name)