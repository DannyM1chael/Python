def countingsort(values, max_value):
    counts = [0] * (max_value + 1)

    for value in values:
        counts[value] += 1
    
    index = 0
    for i in range(max_value + 1):
        for j in range(counts[i]):
            values[index] = i
            index += 1

data = [8, 9, 10, 1, 0, 23, 58]
countingsort(data, 58)
print(data)