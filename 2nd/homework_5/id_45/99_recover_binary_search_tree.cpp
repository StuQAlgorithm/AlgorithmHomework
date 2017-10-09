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
    TreeNode *n1 = NULL, *n2 = NULL;
    TreeNode *pre = new TreeNode(INT_MIN);

    void recoverTree(TreeNode* root) {
        if (!root)
            return;
        inorder(root);
        swap(n1->val, n2->val);
    }

    void inorder(TreeNode *root) {
        if (!root)
            return;
        inorder(root->left);
        if (!n1 && pre->val >= root->val)
            n1 = pre;
        if (n1 && pre->val >= root->val)
            n2 = root;
        pre = root;
        inorder(root->right);
    }
};
