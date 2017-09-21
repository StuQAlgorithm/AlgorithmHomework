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
        List<Integer> ret = new ArrayList<Integer>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();

        if(root == null) return ret;

        int size = 1;
        q.add(root);

        while(q.size() > 0){
            int maxVal = Integer.MIN_VALUE;

            for(int i = 0; i < size; i++){
                TreeNode node = q.poll();
                maxVal = Math.max(node.val, maxVal);

                if(node.left != null) q.add(node.left);
                if(node.right != null) q.add(node.right);
            }

            size = q.size();
            ret.add(maxVal);
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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ret = new ArrayList<Integer>();
        travel(ret, root, 0);
        return ret;
    }

    public void travel(List<Integer> ret, TreeNode root, int level){
        if(root == null) return;

        if(ret.size() < level+1){
            ret.add(Integer.MIN_VALUE);
        }

        ret.set(level, Math.max(root.val, ret.get(level)));

        travel(ret, root.left, level+1);
        travel(ret, root.right, level+1);
    }

}