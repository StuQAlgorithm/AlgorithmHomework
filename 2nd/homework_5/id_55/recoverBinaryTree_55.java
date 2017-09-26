/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode first = null;
    TreeNode second = null;
    TreeNode prev = null;

    public void recoverTree(TreeNode root) {
        if(root == null) return;

        travel(root);

        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }

    public void travel(TreeNode root){
        if(root == null) return;

        travel(root.left);

        if(prev != null && prev.val > root.val){
            if(first == null) first = prev;
            second = root;
        }
        prev = root;

        travel(root.right);
    }
}