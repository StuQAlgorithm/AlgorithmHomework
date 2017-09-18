
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
    
    // 根节点为null怎么办？ 叶子节点为null又怎么办。
    // 思路： DFS，没什么特别的吧。
    
    boolean result = false;
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null) {
            return false;
        }
        if (root.left == null && root.right == null) {
            return root.val == sum ? true : false;
        }
        
        boolean left = hasPathSum(root.left, sum - root.val);
        
        return left == true ? true : hasPathSum(root.right, sum - root.val);
    }
}
