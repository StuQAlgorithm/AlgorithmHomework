/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        return findPathSum(root, sum, 0);
    }
    bool findPathSum(TreeNode* root, int sum, int cursum) {
        if (!root)
            return false;
        if (!root->left && !root->right) {
            if (cursum + root->val == sum )
                return true;
            return false;
        }

        bool result = findPathSum(root->left, sum, cursum + root->val) ||
            findPathSum(root->right, sum, cursum + root->val);
        return result;
    }
};
