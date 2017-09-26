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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root)
            return NULL;
        if (root == p || root == q) //Attention: don't compare root->val with p->val and q->val
            return root;
        TreeNode *l = lowestCommonAncestor(root->left, p, q);
        TreeNode *r = lowestCommonAncestor(root->right, p, q);
        if (l && r)
            return root;
        return !l? r : l;
    }
};
