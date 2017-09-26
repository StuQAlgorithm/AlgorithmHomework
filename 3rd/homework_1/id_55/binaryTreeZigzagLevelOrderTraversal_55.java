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
    //not rescusive
    Queue<TreeNode> q = new LinkedList<TreeNode>();

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<>();

        if(root == null) return ret;

        q.add(root);
        int size = 1;
        boolean orderToLeft = true;

        while(q.size () > 0){
            LinkedList<Integer> list = new LinkedList<Integer>();

            //every level of the tree, pollQueue ${size} times, ${size} eq upper level addQueue times
            for(int i = 0; i < size; i++){
                TreeNode node = q.poll();
                if(orderToLeft){
                    list.add(node.val);
                }else{
                    list.push(node.val);
                }

                if(node.left != null) q.add(node.left);
                if(node.right != null) q.add(node.right);
            }

            size = q.size();
            orderToLeft = !orderToLeft;
            ret.add(list);
        }

        return ret;
    }

}



/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution2 {
    //rescusive
    //create the collect list before the level visit; when visit node, add or push to the right collect
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<>();

        travel(root, ret, 0);

        return ret;
    }

    public void travel(TreeNode root, List<List<Integer>> ret, int level){
        if(root == null) return;

        if(ret.size() < level+1){
            List<Integer> list = new LinkedList<Integer>();
            ret.add(list);
        }

        List<Integer> list = ret.get(level);
        if(level%2 == 0) list.add(root.val);
        else list.add(0, root.val);

        travel(root.left, ret, level+1);
        travel(root.right, ret, level+1);
    }


}