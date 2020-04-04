class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)

        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.front_index == -1:
            return None
        return self.arr[self.front_index]

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def _handle_queue_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2 * len(old_arr))]
        index = 0

        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index

queue = Queue(4)
queue.enqueue(4)
queue.enqueue(9)
queue.enqueue(-5)
queue.enqueue(3)
queue.enqueue(-6)
# queue.enqueue(12)
# queue.enqueue(10)

# queue.dequeue()
print(queue.arr)
print(queue.front())
