"""
Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some
starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def __init__(self):
        self.maxValue = -sys.maxsize
    def helper(self, root):
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.maxValue = max(self.maxValue, left + right + root.val)
        return max(left, right) + root.val
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.maxValue
