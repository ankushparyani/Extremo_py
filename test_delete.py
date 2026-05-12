grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}

grades.update({'Alice': 95})

print("average grade:", sum(grades.values()) / len(grades))

for name, grade in grades.items():
    print(f'{name}: {grade}, average grade: {sum(grades.values()) / len(grades)}')

#print name, grade and average grade for name, grade in grades.items():
    #print(f'{name}: {grade}, average grade: {sum(grades.values()) / len(grades)}')
