# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# path + [root.val]  vs  path.append() ???


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype:   [List[int]]
        """

        result = []
        self.findPath(root, sum, [], result)
        return result

    def findPath(self, root, rest, path, result):
        if not root:
            return
        if not root.left and not root.right and root.val == rest:
            result.append(path + [root.val])
        self.findPath(root.left, rest - root.val,
                    path + [root.val], result)
        self.findPath(root.right, rest - root.val,
                    path + [root.val], result)
