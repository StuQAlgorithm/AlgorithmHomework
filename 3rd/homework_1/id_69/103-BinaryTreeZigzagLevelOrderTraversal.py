# Given a binary tree, return the zigzag level order traversal of
 # its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        direction = 1
        last_size = 1
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            for i in range(last_size):
                node = queue.popleft()
                level.append(node.val)
                if direction < 0:
                    if node.right: queue.append(node.right)
                    if node.left: queue.append(node.left)
                else:
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            res.append(level)
            direction = -direction
            queue.reverse()
            last_size = len(queue)
        return res

