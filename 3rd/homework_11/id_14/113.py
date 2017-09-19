"""
Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, results, root, sum, path):
        path.append(root.val)
        if not root.left and not root.right:
            if sum == root.val:
                results.append(path[:])
        if root.left:
            self.helper(results, root.left, sum - root.val, path)
        if root.right:
            self.helper(results, root.right, sum - root.val, path)
        path.pop()
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        path = []
        results = []
        self.helper(results, root, sum, path)
        return results

