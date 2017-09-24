//Solution 1: brute force search, TLE
class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> result;
        if (board.size() == 0 || board[0].size() == 0 || words.size() == 0)
            return result;
        int n = board.size();
        int m = board[0].size();
        int w = words.size();
        string word;
        bool found;
        for (int k = 0; k < w; ++k) {
            word = words[k];
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (found = findword(board, i, j, word, 0))
                        break;
                }
                if (found) {
                    result.push_back(word);
                    break;
                }
            }
        }
        return result;
    }

    bool findword(vector<vector<char>>& board, int i, int j, string& word, int len) {
        if (len == word.length())
            return true;

        if (i < 0 || j < 0 || i == board.size() || j == board[0].size())
            return false;

        if (board[i][j] != word[len])
            return false;

        board[i][j] ^= 128;
        bool res = findword(board, i-1, j, word, len+1) ||
            findword(board, i+1, j, word, len+1) ||
            findword(board, i, j-1, word, len+1) ||
            findword(board, i, j+1, word, len+1);

        board[i][j] ^= 128;
        return res;
    }
};

//Solution 2: Trie
struct TrieNode {
    bool isWord;
    vector<TrieNode*> child;
    TrieNode() : isWord(false), child(vector<TrieNode*>(26, NULL)) {}
};

class Trie {
public:
    TrieNode* createTrie(vector<string>& words) {
        TrieNode *root = new TrieNode();
        TrieNode *cur;
        int wordsNum, wordLen;
        wordsNum = words.size();
        for (int i = 0; i < wordsNum; ++i) {
            wordLen = words[i].length();
            cur = root;
            for (int j = 0; j < wordLen; ++j) {
                if (!cur->child[words[i][j] - 'a']) 
                    cur->child[words[i][j] - 'a'] = new TrieNode();
                cur = cur->child[words[i][j] - 'a'];
            }
            cur->isWord = true;
        }
        return root;
    }
};

class Solution {
public:
    set<string> se;
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        if (board.size() == 0 || board[0].size() == 0 || words.size() == 0)
            return vector<string>();

        Trie trie;
        TrieNode *root = trie.createTrie(words);
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j)
                findWord(board, i, j, root, "");
        }
        vector<string> result(se.begin(), se.end());
        return result;
    }
    void findWord(vector<vector<char>>& board, int i, int j, TrieNode *root, string cur) {
        if (i < 0 || j < 0 || i == board.size() || j == board[0].size())
            return;
        if (!(board[i][j] >= 'a' && board[i][j] <= 'z'))
            return;
        if (root->child[board[i][j]-'a']) {
            root = root->child[board[i][j]-'a'];
            cur += board[i][j];
            if (root->isWord)
                se.insert(cur);
            board[i][j] ^= 128; //Attention: prevent revisiting previous points in the same search way
            findWord(board, i + 1, j, root, cur);
            findWord(board, i - 1, j, root, cur);
            findWord(board, i, j + 1, root, cur);
            findWord(board, i, j - 1, root, cur);
            board[i][j] ^= 128; //recovery the board[i][j] to its original val
        }
        return;
    }
};
