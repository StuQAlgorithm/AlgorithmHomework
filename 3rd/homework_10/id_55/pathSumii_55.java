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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> ret = new ArrayList<>();
        findPath(root, ret, new ArrayList<Integer>(), sum);
        return ret;
    }

    public void findPath(TreeNode root, List<List<Integer>> ret, List<Integer> list, int sum){
        if(root == null) return;

        list.add(root.val);

        if(root.left == null && root.right == null && root.val == sum){
            ret.add(new ArrayList(list));
        }else{
            findPath(root.left, ret, list, sum - root.val);
            findPath(root.right, ret, list, sum - root.val);
        }

        list.remove(list.size() - 1);
    }


}