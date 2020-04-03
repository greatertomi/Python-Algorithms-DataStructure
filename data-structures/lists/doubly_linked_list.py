class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        else:
            self.tail.next = new_node
            self.tail.next.previous = self.tail
            self.tail = new_node
        return

linked_list = DoublyLinkedList()
linked_list.append(4)
linked_list.append(6)
linked_list.append(9)
linked_list.append(-3)

# Going forward through the list
node = linked_list.head
while node:
    print(node.value)
    node = node.next
print('---------------------')
# Going Backwards through the list
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
