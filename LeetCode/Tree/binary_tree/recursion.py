from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 先序遍历
class preSolution(object):

    def orderTraversal(self, root: TreeNode) -> List[int]:
        self.vals = []
        self.preOrder(root)
        return self.vals

    def preOrder(self, root: TreeNode):
        if not root:
            return
        self.vals.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)


# 中序遍历
class midSolution(object):

    def orderTraversal(self, root: TreeNode) -> List[int]:
        self.vals = []
        self.midorder(root)
        return self.vals

    def midorder(self, root: TreeNode):
        if not root:
            return
        self.midorder(root.left)
        self.vals.append(root.val)
        self.midorder(root.right)


class postSolution(object):
    def orderTraversal(self, root: TreeNode) -> List[int]:
        self.vals = []
        self.postOrder(root)
        return self.vals

    def postOrder(self, root: TreeNode):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.vals.append(root.val)


if __name__ == '__main__':
    # root = [1, None, 2, 3]
    root = TreeNode(1, None, TreeNode(2, (TreeNode(3))))
    # root = TreeNode()
    result = postSolution().orderTraversal(root)
    print(result)
