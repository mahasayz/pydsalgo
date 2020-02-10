# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self._arr = []
        self.inorder_traversal(root)
        self._ptr = 0

    def inorder_traversal(self, root: TreeNode):
        if not root:
            return
        self.inorder_traversal(root.left)
        self._arr.append(root.val)
        self.inorder_traversal(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        idx = self._ptr
        self._ptr += 1
        return self._arr[idx]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._ptr < len(self._arr)
