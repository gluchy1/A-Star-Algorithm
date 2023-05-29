import random

array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(len(array)):
    for j in range(len(array[i])):
        if (i == 0 and j == len(array[i]) - 1) or (i == len(array) - 1 and j == 0):
            continue
        if (i, j) not in [(0, 0), (0, len(array[i]) - 1), (len(array) - 1, 0), (len(array) - 1, len(array[i]) - 1)]:
            if array[i][j] == 0:
                if random.random() < 0.5:
                    array[i][j] = 1

with open("array.txt", "w") as file:
    for row in array:
        file.write(','.join(map(str, row)) + '\n')

print("Tablica została zapisana do pliku array.txt.")
