class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        self.top = Node()
    
    def append(self, value):
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)

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

lst = List()
lst.append(75)
lst.append('hello')
lst.append(True)
lst.append(6)
print(lst)
