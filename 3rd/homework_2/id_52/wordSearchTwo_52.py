class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.count = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        if node.count:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find(board, i, j, ret, trie, pre, visited):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return
            if (i, j) in visited:
                return

            pre += board[i][j]
            if not trie.startsWith(pre):
                return
            if trie.search(pre):
                ret.add(pre)

            visited[(i, j)] = 1
            find(board, i + 1, j, ret, trie, pre, visited)
            find(board, i - 1, j, ret, trie, pre, visited)
            find(board, i, j + 1, ret, trie, pre, visited)
            find(board, i, j - 1, ret, trie, pre, visited)
            del visited[(i, j)]

        if not board or not words:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        ret = set()
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                find(board, i, j, ret, trie, '', visited)

        return list(ret)
