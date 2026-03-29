class TriNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TriNode()

    def insert(self, word: str) -> None:
        '''
        Time Complexity: O(n) n = len of word
        Space Complexity: O(n)
        '''

        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        '''
        Time Complexity: O(n) n = len of word
        Space Complexity: O(n)
        '''

        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        