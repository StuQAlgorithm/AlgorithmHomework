

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
    public List<Integer> largestValues(TreeNode root) {
        // 1.层次遍历找出最大值就好了啊。 用优先级队列去做层次遍历？
        // 2。 思路二， DFS?也不是不可以。每次层次DFS，对应的level，去比较大小，最大的被替换。
        
        //来，dfs写一遍。
        if (root == null) {
            return new ArrayList<>();
        }
        
        List<Integer> ret = new ArrayList<>();
        findLargestValue(root, ret, 0);
        return ret;
        
    }
    
    private void findLargestValue(TreeNode root, List<Integer> ret, int level){
        if(ret.size() -1 < level){  //如果是新的一层。怎么处理，待会看
            ret.add(root.val);
        }
        
        if (root.val > ret.get(level)) {
            ret.set(level, root.val);
        }
        
        
        if(root.left != null) {
            findLargestValue(root.left, ret, level + 1);
        }
        if(root.right != null) {
            findLargestValue(root.right, ret, level + 1);
        }
        
    }
    
    
    
    
    
    
    
    
    
}
