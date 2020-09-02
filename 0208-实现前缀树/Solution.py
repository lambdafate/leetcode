class TrieNode(object):
    def __init__(self):
        self.nexts = [None] * 26 + [False]

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            i = ord(c) - ord('a')
            if p.nexts[i] is None:
                p.nexts[i] = TrieNode()
            p = p.nexts[i]
        p.nexts[-1] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for c in word:
            i = ord(c) - ord('a')
            if p.nexts[i] is None:
                return False
            p = p.nexts[i]
        return p.nexts[-1]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if p.nexts[i] is None:
                return False
            p = p.nexts[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
