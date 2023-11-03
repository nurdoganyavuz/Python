array = [1, 1]

for i in range(18):
    array.append(array[len(array)-1] + array[len(array)-2])

print(array)