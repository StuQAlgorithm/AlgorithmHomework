# Given a binary tree and a sum,
# find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: return False
        if root.val == sum and root.left is None and root.right is None: return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # 注意list的引用
    def findPath(self, root, sum, cur_state):
        if root is None: return
        if root.left is None and root.right is None and root.val == sum: self.res.append(cur_state + [root.val])
        cur_state.append(root.val)
        if root.left: self.findPath(root.left, sum - root.val, cur_state)
        if root.right: self.findPath(root.right, sum - root.val, cur_state)
        cur_state.pop()

    def findPath(self, root, sum, cur_state):
        if root is None: return
        if root.val == sum and root.left is None and root.right is None: self.res.append(cur_state + [root.val])
        # cur_state.append(root.val)
        self.findPath(root.left, sum - root.val, cur_state + [root.val])
        self.findPath(root.right, sum - root.val, cur_state + [root.val])


