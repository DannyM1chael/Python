def is_cross(a, b):
    return (a[1] < b[3] and a[3] > b[1] and a[2] < b[0] and a[0] > b[2])

result = is_cross([-5, 2, 3,-2], [2, 6, 5, 1])
print(result)