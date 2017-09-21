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
        dfs(ret, root, 0);
        return ret;
    }

    private void dfs(List<Integer> ret, TreeNode root, int level) {
        if (root == null) {
            return;
        }
        if (ret.size() < level + 1) {
            ret.add(root.val);
        } else if (root.val > ret.get(level)) {
            ret.set(level, root.val);
        }
        dfs(ret, root.left, level + 1);
        dfs(ret, root.right, level + 1);
    }
}