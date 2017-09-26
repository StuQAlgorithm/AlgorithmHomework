# author: lu19kend
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/


class Solution(object):
    prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
