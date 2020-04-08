class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_____________\n"
            s += "\n_____________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_____________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"
'''
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack)'''

class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

visit_order = list()
stack = Stack()
node = tree.get_root()
stack.push(node)

print(f"""visit_order {visit_order}
stack:{stack}""")

visit_order.append(node.get_value())
print(f"""visit order {visit_order}
{stack} 
""")

print(f"{node} has left child? {node.has_left_child()}")

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order}
stack: 
{stack}
""")

print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")

print(f"{node} has a left child? {node.has_left_child()}")

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order}
stack:
{stack}
""")

visit_order.append(node.get_value())
print(f"visit order {visit_order}")

print(f"{node} has a left child? {node.has_left_child()}")

print(f"{node} has right child? {node.get_right_child()}")

print(stack.pop())
print(stack)

print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")
node = stack.top()
print(node)

print(f"{node} has right child? {node.has_right_child()}")
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)

print(f"""
visit_order {visit_order}
stack
{stack}
""")

print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order: {visit_order}""")

print(f"{node} has left child? {node.has_left_child()}")
print(f"{node} has right child? {node.has_right_child()}")
print(f"pop {stack.pop()} off the stack")

print(f"""
visit_order {visit_order} 
stack
{stack}
""")

print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")

print(f"""stack
{stack}""")

