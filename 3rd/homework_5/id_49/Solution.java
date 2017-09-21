class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ret = new ArrayList<String>();
        generate("", ret, n, n);
        return ret;
    }

    private void generate(String prefix, List<String> ret, int left, int right) {
        if (left > right) {
            return;
        }
        if (left == 0 && right == 0) {
            ret.add(prefix);
            return;
        }
        if (left > 0) {
            generate(prefix + "(", ret, left - 1, right);
        }
        if (right > 0) {
            generate(prefix + ")", ret, left, right - 1);
        }
    }
}