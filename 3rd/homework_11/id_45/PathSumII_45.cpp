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
    deque<int> record;
    vector<vector<int>> result;
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        findPathSum(root, sum);
        return result;
    }
    void findPathSum(TreeNode* root, int sum) {
        if (!root)
            return;

        record.push_back(root->val);
        if (!root->left && !root->right) {
            if (root->val == sum) {
                vector<int> vec(record.begin(), record.end());
                result.push_back(vec);
            }
            record.pop_back();
            return;
        }
        findPathSum(root->left, sum - root->val);
        findPathSum(root->right, sum - root->val);

        record.pop_back();
        return;
    }
};
