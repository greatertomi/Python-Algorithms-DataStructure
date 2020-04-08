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


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

def pre_order(tree: Tree):
    return pre_order_dfs(tree.get_root())

def pre_order_dfs(node: Node):
    if (not node.has_left_child()) and (not node.has_right_child()): # We reached a leaf
        return [node.get_value()]

    lvl_visited = [node.get_value()] # First time we visit the node, it is saved

    if node.has_left_child():
        lvl_visited.extend(pre_order_dfs(node.get_left_child()))

    if node.has_right_child():
        lvl_visited.extend(pre_order_dfs(node.get_right_child()))

    return lvl_visited

print(pre_order(tree))
