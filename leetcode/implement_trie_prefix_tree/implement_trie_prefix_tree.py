"""
https://leetcode.com/problems/implement-trie-prefix-tree/
208. Implement Trie (Prefix Tree)
Medium
--------------------------------
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class TrieNode:
    def __init__(self, val=''):
        self.val = val
        self.child = [None] * 26  # 此处如果使用dict,可以简化代码
        self.isWord = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        if word is None or len(word) == 0 or len(word.strip()) == 0:
            return

        curNode = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curNode.child[index]:
                curNode = curNode.child[index]
            else:
                tmpNode = TrieNode(w)
                curNode.child[index] = tmpNode
                curNode = tmpNode

        curNode.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        if word is None or len(word) == 0 or len(word.strip()) == 0:
            return False
        curNode = self.root
        for w in word:
            index = ord(w) - ord('a')
            if 0 <= index <= 26 and curNode.child[index]:
                curNode = curNode.child[index]
            else:
                return False

        return curNode.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix is None or len(prefix) == 0 or len(prefix.strip()) == 0:
            return True
        curNode = self.root
        for w in prefix:
            index = ord(w) - ord('a')
            if 0 <= index <= 26 and curNode.child[index]:
                curNode = curNode.child[index]
            else:
                return False
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    ret = trie.search("apple")  # returns true
    print(ret)
    ret = trie.search("app")  # returns false
    print(ret)
    ret = trie.startsWith("app")  # returns true
    print(ret)
    trie.insert("app")
    ret = trie.search("app")  # returns true
    print(ret)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    main()
