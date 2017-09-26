# author: lu19kend
# https://leetcode.com/problems/symmetric-tree/description/


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            lnode = queue.pop(0)
            rnode = queue.pop(0)
            if lnode is None and rnode is None:
                continue
            if (lnode is None) ^ (rnode is None):
                return False
            if lnode.val != rnode.val:
                return False
            queue.append(lnode.left)
            queue.append(rnode.right)
            queue.append(lnode.right)
            queue.append(rnode.left)
        return True
