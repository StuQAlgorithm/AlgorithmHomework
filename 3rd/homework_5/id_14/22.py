"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = set()
        if n == 0:
            results.add("")
        else:
            prev = self.generateParenthesis(n - 1)
            print(prev)
            for str in prev:
                for i in range(len(str)):
                    if str[i] == "(":
                        str = str[:i+1] + "()" + str[i+1:]
                        results.add(str)
                        str = str[:i + 1] + str[i + 3:]
                results.add("()" + str)

        return [x for x in results]


s = Solution()
list = s.generateParenthesis(1)
for str in list:
    print(str)

