/**
 *  * Definition for a binary tree node.
 *  * struct TreeNode {
 *  *     int val;
 *  *     TreeNode *left;
 *  *     TreeNode *right;
 *  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 *  * };
 *  */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int> > result;
        deque<TreeNode*> dequ;
        int qu_size;
        bool is_left_right = true;
        TreeNode *t;
        if (root) {
            dequ.push_back(root);
            while (!dequ.empty()) {
                qu_size = dequ.size();
                vector<int> vec;
                if (is_left_right) {
                    while (qu_size--) {
                        t = dequ.front();
                        vec.push_back(t->val);
                        dequ.pop_front();
                        if (t->left)
                            dequ.push_back(t->left);
                        if (t->right)
                            dequ.push_back(t->right);
                    }
                } else {
                    while (qu_size--) {
                        t = dequ.back();
                        vec.push_back(t->val);
                        dequ.pop_back();
                        if (t->right)
                            dequ.push_front(t->right);
                        if (t->left)
                            dequ.push_front(t->left);
                    }
                }
                result.push_back(vec);
                is_left_right = !is_left_right;
            }
        }
        return result;
    }
};
