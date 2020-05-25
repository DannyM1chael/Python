class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def __str__(self):
        return str(self.value)

class SortedList:
    def __init__(self):
        self.top = Node()
    
    def append(self, value):
        current = self.top
        while current.next_node is not None and current.next_node.value < value:
            current = current.next_node

        new_node = Node(value)
        new_node.next_node = current.next_node
        current.next_node = new_node

    def delete(self,value):
        current = self.top.next_node
        prev = self.top
        while current is not None:
            if current.value == value:
                prev.next_node = current.next_node
                return
            
            prev = current
            current = current.next_node

    def __str__(self):
        current = self.top.next_node
        values = "["
        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node
        return values + "]"

lst = SortedList()
lst.append(75)
lst.append(12)
lst.append(28)
lst.append(6)
print(lst)
