class TrieNode():
    def __init__(self):
        self.chars = {}
        self.word = False

class WordDictionary:

    def __init__(self):
      self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = TrieNode()
            cur = cur.chars[c]
        cur.word = True

    def dfs(self, dots):
        if cur.chars:
            return 

    def search(self, word: str) -> bool:
        def dfs(j, child):
            for x in range(j, len(word)):
                if word[x] == ".":
                    for v in child.chars.values():
                        if dfs(x + 1, v):
                            return True
                    return False
                else:
                    w = word[x]
                    if w not in child.chars:
                        return False
                    child = child.chars[w]
            return child.word
        return dfs(0, self.root)
                    