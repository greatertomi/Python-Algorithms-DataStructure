class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        # Move to the tail (the last node)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return

def skip_i_delete_j(head, i, j):
    input_node = head
    trim_link_list = None
    position_counter = 1
    i_mode = True
    last_node = False

    while not last_node:
        if i_mode: # Additive Mode
            if trim_link_list is None:
                trim_link_list = Node(input_node.data)
            else:
                position_tail = trim_link_list
                while position_tail.next:
                    position_tail = position_tail.next
                position_tail.next = Node(input_node.data)

            if position_counter == i:
                i_mode = False
                position_counter = 0
        else:
            if position_counter == j:
                i_mode = True
                position_counter = 0

        position_counter += 1
        last_node = input_node.next is None
        input_node = input_node.next

    return trim_link_list

def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)

# head = create_linked_list(arr)
# print_linked_list(head)
# print_linked_list(skip_i_delete_j(head, 2, 4))

