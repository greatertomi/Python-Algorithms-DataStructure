class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def insert_at_head(linked_list1, value):
    position_tail_continuity = linked_list1.head
    linked_list1.head = Node(value)
    linked_list1.head.next = position_tail_continuity

    return linked_list1


def reverse(linked_list1):
    tail_position = linked_list1.head
    reversed_linked_list = LinkedList()
    while tail_position is not None:
        value = tail_position.value
        reversed_linked_list = insert_at_head(reversed_linked_list, value)
        tail_position = tail_position.next

    return reversed_linked_list

def iscircular(linked_list1):
    if linked_list1.head is None:
        return False
    slow = linked_list1.head
    fast = linked_list1.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

small_loop = LinkedList([0])
list_with_loop = LinkedList([2, -1, 3, 0, 5])
small_loop.head.next = small_loop.head
print("Pass" if iscircular(list_with_loop) else "Fail")
print("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
print("Pass" if not iscircular(LinkedList([1])) else "Fail")
print("Pass" if iscircular(small_loop) else "Fail")
print("Pass" if not iscircular(LinkedList([])) else "Fail")
