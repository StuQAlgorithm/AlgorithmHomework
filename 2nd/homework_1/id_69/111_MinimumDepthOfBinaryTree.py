# author: lu19kend
# https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = []
        queue.append(root)
        last_width = 1
        cur_depth = 1
        while queue:
            while last_width:
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return cur_depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                last_width -= 1
            cur_depth += 1
            last_width = len(queue)
