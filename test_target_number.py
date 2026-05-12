print('please enter a target number')
t = int(input())
print(f'You entered the target number: {t}')

l = [1,2,4,7]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == t:
            print(f'Found a pair at position: {i} and {j}')
