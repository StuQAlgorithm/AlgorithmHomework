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
        
        self.list = []
        self.findDfs(root, 0)
        return 


    def findDfs(self, node, level):
        if not node: return None

        if level == len(self.list):
            self.list.append(node.val)
        else:
            self.list[level] = max(self.list[level], node.val)

        self.findDfs(node.left, level + 1)
        self.findDfs(node.right, level + 1)