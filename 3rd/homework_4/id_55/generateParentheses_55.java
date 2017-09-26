class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ret = new ArrayList<String>();

        if(n == 0) return ret;

        backtrack(ret, "", 0, 0, n);

        return ret;
    }

    public void backtrack(List<String> ret, String str, int open, int close, int max){
        if(str.length() == max*2){
            ret.add(str);
            return;
        }

        if(open < max){
            backtrack(ret, str+"(", open+1, close, max);
        }

        if(close < open){
            backtrack(ret, str+")", open, close+1, max);
        }

    }


}