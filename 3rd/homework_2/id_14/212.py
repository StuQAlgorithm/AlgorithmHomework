"""
Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

# 太慢, 被拒了
class Solution(object):
    def isExists(self, board, word, y, x, location):
        if location == len(word):
            return True
        if y < 0 or x < 0 or y == len(board) or x == len(board[y]):
            return False

        if board[y][x] != word[location]:
            return False
        a = ord('#')
        board[y][x], a = a, board[y][x]
        ret = self.isExists(board, word, y + 1, x, location + 1) \
                or self.isExists(board, word, y - 1, x, location + 1) \
                or self.isExists(board, word, y, x + 1, location + 1) \
                or self.isExists(board,word, y, x - 1, location + 1)
        board[y][x], a = a, board[y][x]
        return ret
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        if not board:
            return []
        results = []
        wordDict = {}
        for word in words:
            if word in wordDict:
                continue

            wordDict[word] = 0

            for y in range(len(board)):
                for x in range(len(board[0])):
                    if self.isExists(board, word, y, x, 0):
                        if wordDict[word] > 0:
                            continue
                        else:
                            wordDict[word] += 1
                            results.append(word)
                            if len(results) == len(words):
                                return results
        return results


board = [
    ['a'],
    ['a']
]
words = ["a"]

s = Solution()
print(s.findWords(board, words))