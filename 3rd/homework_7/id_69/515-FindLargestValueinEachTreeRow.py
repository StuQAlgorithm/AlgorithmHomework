# You need to find the largest value in each row of a binary tree.

# Example:
# Input:

#           1
#          / \
#         3   2
#        / \   \
#       5   3   9

# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        queue = []
        queue.append(root)
        last_size = 1
        res = []
        while queue:
            res.append(max([n.val for n in queue]))
            for i in range(last_size):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            last_size = len(queue)
        return res



