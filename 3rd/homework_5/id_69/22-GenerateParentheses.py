# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# java
# public class Solution
# {
#     public List<String> generateParenthesis(int n)
#     {
#         List<List<String>> lists = new ArrayList<>();
#         lists.add(Collections.singletonList(""));

#         for (int i = 1; i <= n; ++i)
#         {
#             final List<String> list = new ArrayList<>();

#             for (int j = 0; j < i; ++j)
#             {
#                 for (final String first : lists.get(j))
#                 {
#                     for (final String second : lists.get(i - 1 - j))
#                     {
#                         list.add("(" + first + ")" + second);
#                     }
#                 }
#             }

#             lists.add(list);
#         }

#         return lists.get(lists.size() - 1);
#     }
# }

class Solution(object):
# def generateParenthesis(self, n):
#     def generate(p, left, right, parens=[]):
#         if left:         generate(p + '(', left-1, right) # 保证了left一定比right先，不会在数量相同时出现)(这样的情况
#         if right > left: generate(p + ')', left, right-1)
#         if not right:    parens += p
#         return parens
#     return generate('', n, n)

# dp
    def generateParenthesis(self, n):
        lists = []
        lists.append([''])
        for i in range(1, n+1):
            l = []
            for j in range(i):
                for first in lists[j]:
                    for second in lists[i-1-j]:
                        l.append("(" + first + ")" + second)
            lists.append(l)
        return lists[-1]

if __name__ == '__main__':
    print(Solution().generateParenthesis(5))


