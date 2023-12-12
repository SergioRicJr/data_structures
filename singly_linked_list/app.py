# Lista encadeada simples
# Different from array, the order in memory is not sequential

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def set_next():
        pass

    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def length(self):
        if self.head == None:
            return 0
        
        current_node = self.head
        total = 0
        while current_node:
            current_node = current_node.next
            total += 1
        return total
    
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node
    
    def __repr__(self) -> str:
        if self.head == None:
            return '[]'
        items = ''
        current_node = self.head
        while current_node.next != None:
            items += f'{current_node.data}, '
            current_node = current_node.next
        items += f' {current_node.data}'
              
        return '[' + items + ']'            

node1 = 'sergio'
node2 = 'ricardo'
node3 = 'césar'
node4 = 'Augusto'

lista = LinkedList()

lista.append(node1)
lista.append(node2)
lista.append(node3)
lista.append(node4)
lista.reverse()
print(lista)