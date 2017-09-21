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
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        traverse(ret, root, 0);
        return ret;
    }

    public void traverse(List<List<Integer>> ret, TreeNode root, int level) {
        if (root == null) {
            return;
        }

        if (ret.size() < level + 1) {
            ret.add(new LinkedList<Integer>());
        }
        if (level % 2 == 0) {
            ret.get(level).add(root.val);
        } else {
            ret.get(level).add(0, root.val);
        }
        traverse(ret, root.left, level + 1);
        traverse(ret, root.right, level + 1);
    }
}