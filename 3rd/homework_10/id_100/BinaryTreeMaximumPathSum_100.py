# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max = root.val
        self.maxPath(root)
        return self.max

    def maxPath(self, root):
        if not root:
            return 0
        left = max(0, self.maxPath(root.left))
        right = max(0, self.maxPath(root.right))
        self.max = max(self.max, left + right + root.val)
        return max(left, right) + root.val
