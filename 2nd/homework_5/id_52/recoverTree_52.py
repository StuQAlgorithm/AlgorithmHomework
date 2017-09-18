# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    first = None
    second = None
    pre = None
    def midTraverse(self, root):
        if root is None:
            return
        self.midTraverse(root.left)
        if self.pre is not None:
            if self.first is None and self.pre.val > root.val:
                self.first = self.pre
            if self.first is not None and self.pre.val > root.val:
                self.second = root
        self.pre = root
        self.midTraverse(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.midTraverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

