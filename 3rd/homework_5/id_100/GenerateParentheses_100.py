class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self.max = n
        self.backtrack('', 0, 0)
        return self.list

    def backtrack(self, str, open, close):
        if len(str) == self.max * 2:
            self.list.append(str)
            return

        if open < self.max:
            self.backtrack(str + '(', open + 1, close)
        if close < open:
            self.backtrack(str + ')', open, close + 1)
