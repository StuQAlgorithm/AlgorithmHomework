
class Solution {
    public List<String> generateParenthesis(int n) {
        
        //好像没什么具体思路啊。。如果去穷举？
        // 思路1.构建一颗 level = 2*n 的树，每一棵树的左孩子都是左括号，右孩子都是右括号，根节点为左括号。然后dfs遍历，用stack去匹配。匹配成功则塞回到返回值中。可是建树本身无法完成。。。
        // 看下别人的思路吧。 
        // 没能理解这里面的玄机。。。。多想想吧
        
    
    List<String> list = new ArrayList<String>();
    generateOneByOne("", list, n, n);
    return list;
}
public void generateOneByOne(String sublist, List<String> list, int left, int right){
    if(left > right){
        return;
    }
    if(left > 0){
        generateOneByOne( sublist + "(" , list, left-1, right);
    }
    if(right > 0){
        generateOneByOne( sublist + ")" , list, left, right-1);
    }
    if(left == 0 && right == 0){
        list.add(sublist);
        return;
    }
}
}
