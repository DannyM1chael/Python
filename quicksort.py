def quicksort(array, start, end):
    if start >= end:
        return
    divider = array[start]

    before, after = [],[]
    i = start + 1
    while i < end + 1:
        if array[i] < divider:
            before.append(array[i])
        else:
            after.append(array[i])
        i += 1
    
    index = start
    while len(before) > 0:
        array[index] = before.pop()
        index += 1
    
    array[index] = divider
    midpoint = index

    index += 1
    while len(after) > 0:
        array[index] = after.pop()
        index += 1
    
    quicksort(array, start, midpoint - 1)
    quicksort(array, midpoint + 1, end)
