# Priority Queue implemented using MinHeap
import math

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f"Issue({self.value}, {self.priority})"

    def __str__(self):
        return f"Issue({self.value}, {self.priority})"

class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        self.values.append(Node(value, priority))
        self.bubble_up()

    def bubble_up(self):
        index = len(self.values) - 1
        element = self.values[index]
        while index > 0:
            parentIndex = math.floor((index - 1)/2)
            parent = self.values[parentIndex]
            if element.priority >= parent.priority:
                break
            self.values[parentIndex] = element
            self.values[index] = parent
            index = parentIndex

    def dequeue(self):
        min_value = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()
        return min_value

    def sink_down(self):
        index = 0
        length = len(self.values)
        element = self.values[0]

        while True:
            print('hello')
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2
            leftChild = None
            rightChild = None
            swap = None

            if leftChildIndex < length:
                leftChild = self.values[leftChildIndex]
                if leftChild.priority < element.priority:
                    swap = leftChildIndex

            if rightChildIndex < length:
                rightChild = self.values[rightChildIndex]
                if (swap is None and rightChild.priority < element.priority) \
                        or (swap is not None and rightChild.priority < leftChild.priority):
                    swap = rightChildIndex

            if swap is None:
                break

            self.values[index] = self.values[swap]
            self.values[swap] = element
            index = swap


pr_queue = PriorityQueue()
pr_queue.enqueue('Heat', 5)
pr_queue.enqueue('Warm', 3)
pr_queue.enqueue('Computer', 1)
pr_queue.enqueue('Bed', 4)
pr_queue.enqueue('Paper', 2)
pr_queue.enqueue('Fan', 8)
pr_queue.enqueue('Biro', 6)
# print(pr_queue.values)

pr_queue.dequeue()
print(pr_queue.values)

