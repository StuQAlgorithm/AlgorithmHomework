
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        //思路一： 和level order traversal 一样。 只是交替的变换一下顺序？
        
        
        Queue<TreeNode> parentQueue = new LinkedList<>();
        Queue<TreeNode> childrenQueue = new LinkedList<>();
        
        if (root == null) {
            return new ArrayList<>();
        }
        
        List<List<Integer>> list = new ArrayList<>();
        List<Integer> subList = new ArrayList<>();
        parentQueue.add(root);
        int level = 0;
        while (!parentQueue.isEmpty()) {
            TreeNode node = parentQueue.poll();
             if(level % 2 == 1) {
                subList.add(0,node.val);
             } else {
                 subList.add(node.val);
             }
            
            if(node.left != null) {
                childrenQueue.add(node.left);
            }
            if(node.right != null) {
                childrenQueue.add(node.right);
            }
           
           
            if(parentQueue.isEmpty()) {

                parentQueue = childrenQueue;
                childrenQueue= new LinkedList<>();
               
                  
                list.add(subList);
                subList = new ArrayList<>();
                level ++;
            }
        
        }
        return list;
        
    }
}
