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
    int result = INT_MIN;
    int maxPathSum(TreeNode* root) {
        findMaxPathSum(root);
        return result;
    }
    int findMaxPathSum(TreeNode* root) {
        if (!root)
            return 0;
        int leftSum = max(0, findMaxPathSum(root->left));
        int rightSum = max(0, findMaxPathSum(root->right));

        result = max(result, root->val + leftSum + rightSum);
        return root->val + max(leftSum, rightSum);
    }
};
