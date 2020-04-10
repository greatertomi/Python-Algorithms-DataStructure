import math


class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def insert(self, element):
        self.values.append(element)
        self.bubble_up()

    def bubble_up(self):
        index = len(self.values) - 1
        element = self.values[index]
        while index > 0:
            parentIndex = math.floor((index - 1) / 2)
            parent = self.values[parentIndex]
            if element <= parent:
                break
            self.values[parentIndex] = element
            self.values[index] = parent
            index = parentIndex

    def extract_max(self):
        max_value = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()
        return max_value

    def sink_down(self):
        index = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2
            leftChild = None
            rightChild = None
            swap = None

            if leftChildIndex < length:
                leftChild = self.values[leftChildIndex]
                if leftChild > element:
                    swap = leftChildIndex

            if rightChildIndex < length:
                rightChild = self.values[rightChildIndex]
                if (swap is None and rightChild > element) or (swap is not None and rightChild > leftChild):
                    swap = rightChildIndex

            if swap is None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = element
            index = swap

heap = MaxBinaryHeap()
heap.insert(15)
heap.insert(30)
heap.insert(42)
heap.insert(19)
heap.insert(31)
heap.insert(9)
heap.insert(50)
heap.insert(35)

# heap.extract_max()

print(heap.values)
