class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    # 广度优先添加
    def add_element(self, value_element):
        # value_element 为加入的节点
        node = Node(value_element)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while True:
            pop_node = queue.pop(0)
            if not pop_node.left:
                pop_node.left = node
                return
            else:
                queue.append(pop_node.left)
            if not pop_node.right:
                pop_node.right = node
                return
            else:
                queue.append(pop_node.right)

    def BFS(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            pop_node = queue.pop(0)
            print(pop_node.value)
            if pop_node.left:
                queue.append(pop_node.left)
            if pop_node.right:
                queue.append(pop_node.right)


tree = Tree()
tree.add_element(1)
tree.add_element(3)
tree.add_element(6)
tree.add_element(2)
tree.add_element(10)
tree.BFS()
