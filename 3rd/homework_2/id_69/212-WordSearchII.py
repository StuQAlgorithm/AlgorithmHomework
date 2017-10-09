# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

# click to show hint.

# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

# If the current candidate does not exist in all words' prefix,
# you could stop backtracking immediately.
# What kind of data structure could answer such query efficiently?
# Does a hash table work? Why or why not? How about a Trie?
# If you would like to learn how to implement a basic trie,
# please work on this problem: Implement Trie (Prefix Tree) first.

# 1. prepare words trie tree or hash map, then use DFS traversal the board---> N(wk + NMk)


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        word_map = self.build_map(words)
        row_len = len(board)
        col_len = len(board[0])
        res = []
        for r in range(row_len):
            for c in range(col_len):
                node = self.dfs(word_map, board, r, c, res)
        return res

    def dfs(self, wmap, board, r, c, res):
      l = board[r][c]
      if l == '#' or l not in wmap: return
      if wmap[l].get(None, None):
          res.append(wmap[l].pop(None))
      board[r][c] = '#'
      if r < len(board) - 1: self.dfs(wmap[l], board, r+1, c, res)
      if r > 0: self.dfs(wmap[l], board, r-1, c, res)
      if c < len(board[0]) - 1: self.dfs(wmap[l], board, r, c+1, res)
      if c > 0: self.dfs(wmap[l], board, r, c-1, res)
      board[r][c] = l

    def build_map(self, words):
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = word
        return root

# class Solution(object):
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         trie = {}
#         for w in words:
#             t = trie
#             for c in w:
#                 if c not in t:
#                     t[c] = {}
#                 t = t[c]
#             t['#'] = w
#         ret = set()
#         rows, cols = len(board), len(board[0])
#         used = [[False for _ in range(cols)] for _ in range(rows)]

#         def dfs(i, j, tries):
#             used[i][j] = True
#             next_tries = tries[board[i][j]]
#             if '#' in next_tries:
#                 ret.add(next_tries['#'])
#             if i-1 >= 0 and not used[i-1][j] and board[i-1][j] in next_tries: dfs(i - 1, j, next_tries)
#             if i+1 < rows and not used[i+1][j] and board[i+1][j] in next_tries: dfs(i + 1, j, next_tries)
#             if j-1 >= 0 and not used[i][j-1] and board[i][j-1] in next_tries: dfs(i, j - 1, next_tries)
#             if j+1 < cols and not used[i][j+1] and board[i][j+1] in next_tries:  dfs(i, j + 1, next_tries)
#             used[i][j] = False

#         for i in range(rows):
#             for j in range(cols):
#                 if board[i][j] in trie:
#                     dfs(i, j, trie)
#         return list(ret)

if __name__ == '__main__':
  s = Solution()
#   print(s.findWords([
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ], ["oath","pea","eat","rain"]))
  print(s.findWords([['a']],['a']))
