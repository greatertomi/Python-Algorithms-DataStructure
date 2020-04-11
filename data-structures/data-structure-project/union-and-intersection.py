class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(list1, list2):
    list_union = []
    list1_head = list1.head
    while list1_head:
        list1_head_value = int(list1_head.value)
        list_union.append(list1_head_value)
        list1_head = list1_head.next

    list2_head = list2.head
    while list2_head:
        list2_head_value = int(list2_head.value)
        if list2_head_value not in list_union:
            list_union.append(list2_head_value)
        list2_head = list2_head.next

    list_union.sort()
    return list_union

def to_list(input_list):
    return_list = []
    head = input_list.head
    while head:
        return_list.append(head.value)
        head = head.next

    return return_list

def intersection(list1, list2):
    list1 = to_list(list1)
    list2 = to_list(list2)
    intersection_list = []

    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                intersection_list.append(num1)

    return intersection_list

linked_list = LinkedList()
linked_list.append(4)
linked_list.append(6)
linked_list.append(8)
linked_list.append(9)
linked_list.append(12)

linked_list2 = LinkedList()
linked_list2.append(2)
linked_list2.append(6)
linked_list2.append(9)
linked_list2.append(10)
linked_list2.append(12)
linked_list2.append(13)

# print(to_list(linked_list))
# print(linked_list2)

print('union', union(linked_list, linked_list2))
print('intersection', intersection(linked_list, linked_list2))
