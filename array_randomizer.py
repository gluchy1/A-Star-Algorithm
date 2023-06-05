try:
    import random
except:
    pass

array = [[1]*10 for _ in range(10)]
path = [(0, 0)]
while path[-1] != (9, 9):
    i, j = path[-1]
    if i == 9:
        path.append((i, j+1))
    elif j == 9:
        path.append((i+1, j))
    elif random.random() < 0.5:
        path.append((i, j+1))
    else:
        path.append((i+1, j))

for i, j in path:
    array[i][j] = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        if (i, j) in path:
            continue
        if random.random() < 0.5:
            array[i][j] = 0

with open("array.txt", "w") as file:
    for row in array:
        file.write(','.join(map(str, row)) + '\n')

print("New Array generated")
