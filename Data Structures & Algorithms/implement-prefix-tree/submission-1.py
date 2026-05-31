class PrefixNode:
    def __init__(self):
        self.chars = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()    

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = PrefixNode()
            cur = cur.chars[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return True
        