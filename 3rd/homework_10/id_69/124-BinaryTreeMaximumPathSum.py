# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from
# some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# int maxPathSum(TreeNode *root) {
#     int maxPath = INT_MIN;
#     dfsMaxPath(root, maxPath);
#     return maxPath;
# }

# int dfsMaxPath(TreeNode *root, int &maxPath) {
#     if (!root) return 0;
#     int l = max(0, dfsMaxPath(root->left, maxPath));
#     int r = max(0, dfsMaxPath(root->right, maxPath));
#     maxPath = max(maxPath, l + r + root->val);
#     return root->val + max(l, r);
# }

# 对任意节点：找到左右子树的最大值，在加上root
import sys
class Solution(object):
    def __init__(self):
        self.max_path_sum = -sys.maxsize - 1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.dfs(root)
        return self.max_path_sum

    def dfs(self, root):
        left_max = max(0, self.dfs(root.left)) if root.left else 0
        right_max = max(0, self.dfs(root.right)) if root.right else 0
        self.max_path_sum = max(self.max_path_sum, left_max+right_max+root.val)
        return root.val + max(left_max, right_max)



