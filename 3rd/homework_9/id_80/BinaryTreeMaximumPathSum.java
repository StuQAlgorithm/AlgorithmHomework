

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
    
        
        
        // 我把path sum 1,2,3都做出来了。
        // 现在要做这道题，可以借鉴的是什么了？1. 我应该需要遍历所有的节点。针对每个节点DFS， 得出的最大值中的最大值，就是结果
        //  可是作为一棵树，怎么从child节点，DFS了。。
        // 等等， 是不是应该算，每一个节点的左子树最大path，和右子树最大path，之和，然后求解？
        // 超时了，没有具体答案， 看别人的吧。
        
    int maxValue;
    
    public int maxPathSum(TreeNode root) {
        maxValue = Integer.MIN_VALUE;
        maxPathDown(root);
        return maxValue;
    }
    
    private int maxPathDown(TreeNode node) {
        if (node == null) return 0;
        int left = Math.max(0, maxPathDown(node.left));
        int right = Math.max(0, maxPathDown(node.right));
        maxValue = Math.max(maxValue, left + right + node.val);
        return Math.max(left, right) + node.val;
    }
        
    
}
