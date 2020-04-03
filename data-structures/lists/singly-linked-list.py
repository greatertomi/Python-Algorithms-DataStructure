class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = new_node
        return

    def search(self, value):
        search_node = Node(value)
        found_node_value = None

        if self.head is None:
            return -1
        current_node = self.head
        while current_node.next:
            if search_node.value == current_node.value:
                found_node_value = current_node
                break
            current_node = current_node.next

        if found_node_value is None:
            return -1
        else:
            return found_node_value

    def shift(self):
        if self.head is None:
            return None
        current_head = self.head
        self.head = self.head.next
        return current_head

    def remove(self, value):
        remove_node = Node(value)
        removed_checker = 0
        if self.head.value is None:
            return -1
        # if remove_node.value == self.head.value:
        #     remove_head = self.head
        #     self.head = self.head.next
        #     remove_head.next = None
        #     return 1

        current_node = self.head.next
        previous_node = self.head
        while current_node.next:
            if current_node.value == remove_node.value:
                previous_node.next = current_node.next
                current_node.next = None
                removed_checker = 1
                break
            previous_node = current_node
            current_node = current_node.next
        return removed_checker

    def pop(self):
        first_node = self.head.value
        self.head = self.head.next
        return first_node

    def insert(self, value, position):
        new_node = Node(value)
        count = 0
        current_node = self.head.next
        previous_node = self.head
        while current_node.next and count <= value:
            if count == value:
                previous_node.next = new_node
                new_node.next = current_node
                break
            count += 1
        return

    # Converts linked list to python list
    def to_list(self):
        list1 = []
        if self.head is None:
            return

        node = self.head
        while node:
            list1.append(node.value)
            node = node.next

        return list1

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


linked_list = SinglyLinkedList()
linked_list.append(-1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(9)
linked_list.append(12)

print(linked_list)
# node = linked_list.head
# linked_list.insert(25, 2)
# # print(linked_list.to_list())
# while node:
#     print(node.value)
#     node = node.next
