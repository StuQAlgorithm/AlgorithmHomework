# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.result = []
        self.travel(root, 0)
        return self.result

    def travel(self, curr, level):
        result = self.result
        if not curr:
            return
        elif len(result) <= level:
            result.append([curr.val])
        elif level % 2 == 0:
            result[level].extend([curr.val])
        else:
            result[level].insert(0, curr.val)

        self.travel(curr.left, level + 1)
        self.travel(curr.right, level + 1)
