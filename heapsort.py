def heapsort(values):
    make_heap(values)
    i = 0
    while i < len(values):
        last = (len(values) - 1) - i
        values[0], values[last] = values[last], values[0]
        remake_heap(values, latest_index = last - 1)
        i += 1

def make_heap(values):
    i = 0
    while i < len(values):
        index= i
        while index != 0:
            parent_index = (index - 1) // 2
            if values[index] <= values[parent_index]:
                break
            values[index], values[parent_index] = values[parent_index], values[index]
            index = parent_index
        i += 1

def remake_heap(values, latest_index):
    index = 0
    while True:
        child1_idx = 2 * index + 1
        child2_idx = 2 * index + 2

        if child1_idx >= latest_index:
            child1_idx = index
        if child2_idx >= latest_index:
            child2_idx = index
        
        if(values[index] >= values[child1_idx]) and (values[index] >= values[child1_idx]):
            break

        if values[child1_idx] > values[child2_idx]:
            swap_child_idx = child1_idx
        else:
            swap_child_idx = child2_idx
        
        values[index], values[swap_child_idx] = values[swap_child_idx], values[index]
        index = swap_child_idx

array = [7, 8, 15, 2, 0, 36, 1]
heapsort(array)
print(array)

    