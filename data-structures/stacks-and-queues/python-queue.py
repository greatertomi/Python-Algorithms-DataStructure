class Queue:
    def __init__(self):
        self.arr = []

    def size(self):
        return len(self.arr)

    def enqueue(self, value):
        self.arr.append(value)

    def dequeue(self):
        return self.arr.pop(0)

    def reverse(self):
        return self.arr[::-1]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.arr)
print(q.reverse())
# lp = [10, 15, 20, 25]
# print(lp[::-1])


# # Test size
# print("Pass" if (q.size() == 3) else "Fail")
#
# # Test dequeue
# print("Pass" if (q.dequeue() == 1) else "Fail")
#
# # Test enqueue
# q.enqueue(4)
# print("Pass" if (q.dequeue() == 2) else "Fail")
# print("Pass" if (q.dequeue() == 3) else "Fail")
# print("Pass" if (q.dequeue() == 4) else "Fail")
# q.enqueue(5)
# print("Pass" if (q.size() == 1) else "Fail")
