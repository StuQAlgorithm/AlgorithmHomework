/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Solution 1: bfs
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

//Solution 2: dfs
class Solution {
public:
    vector<int> result;
    vector<int> largestValues(TreeNode* root) {
        findLargestVal(root, 1); 
        return result;
    }   
    void findLargestVal(TreeNode* root, int layer) {
        if (!root)
            return;
        if (result.size() < layer) {
            result.push_back(root->val);
        } else if (root->val > result[layer-1]) {
            result[layer-1] = root->val;
        }   

        findLargestVal(root->left, layer + 1); 
        findLargestVal(root->right, layer + 1); 
    }
};
