from Node import Node
class LinkedList:
    

    def __init__(self):
        self.head = None

    
    def __len__(self):
        
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def __getitem__(self, index):
        
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data
   
    def __str__(self):
        
        if self.head is None:
            return "LinkedList: Empty"
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "LinkedList: " + " -> ".join(elements)