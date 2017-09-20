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
    vector<int> largestValues(TreeNode* root) {
        vector<int> result;
        queue<TreeNode *>qu;
        int n, curmax;
        TreeNode *t;
        if (root) {
            qu.push(root);
            while (!qu.empty()) {
                n = qu.size();
                curmax = INT_MIN;
                while (n--) {
                    t = qu.front();
                    qu.pop();
                    if (t->val > curmax)
                        curmax = t->val;
                    if (t->left)
                        qu.push(t->left);
                    if (t->right)
                        qu.push(t->right);
                }
                result.push_back(curmax);
            }
        }
        return result;
    }
};
