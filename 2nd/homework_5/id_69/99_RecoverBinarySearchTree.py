# https://leetcode.com/problems/recover-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution(object):

    def __init__(self):
        self.prev = TreeNode(-sys.maxsize - 1)
        self.first = None
        self.second = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.in_order_traversal(root)
        if self.first is not None and self.second is not None:
            self.first.val, self.second.val = self.second.val, self.first.val

    def in_order_traversal(self, root):
        if root is None:
            return
        self.in_order_traversal(root.left)
        if self.first is None and root.val <= self.prev.val:
            self.first = self.prev
        if self.first is not None and root.val <= self.prev.val:
            self.second = root
        self.prev = root
        self.in_order_traversal(root.right)
