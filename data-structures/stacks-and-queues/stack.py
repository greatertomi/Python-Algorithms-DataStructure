class Stack(object):
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        if self.next_index == len(self.arr):
            print('Out of space! Increasing array capacity...')
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2*len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def size(self):
        return self.num_elements

    def is_empty(self):
        if self.num_elements == 0:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None

        self.arr[self.num_elements - 1] = 0
        self.num_elements -= 1
        self.next_index -= 1
        return self.arr[self.next_index]

foo = Stack(5)
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
print(foo.arr)
foo.pop()
foo.push(-4)
print(foo.arr)
# print(foo.size())
# print(foo.is_empty())

