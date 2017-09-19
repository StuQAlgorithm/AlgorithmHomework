class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = self.makeTrieTree({}, words)
        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, '')
        return list(self.res)

    def dfs(self, board, i, j, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.dfs(board, i + 1, j, trie[board[i][j]], pre + board[i][j])
            self.dfs(board, i - 1, j, trie[board[i][j]], pre + board[i][j])
            self.dfs(board, i, j + 1, trie[board[i][j]], pre + board[i][j])
            self.dfs(board, i, j - 1, trie[board[i][j]], pre + board[i][j])
            self.used[i][j] = False

    def makeTrieTree(self, trie, words):
        for word in words:
            t = trie
            for letter in word:
                if letter not in t:
                    t[letter] = {}
                t = t[letter]
            t['#'] = '#'

        return trie
