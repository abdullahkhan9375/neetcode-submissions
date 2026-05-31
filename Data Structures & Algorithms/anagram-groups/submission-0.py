class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for word in strs:
            sr_word = "".join(sorted(word))
            if sr_word in di.keys():
                di[sr_word].append(word)
            else:
                di[sr_word] = [word]

        lol = []
        for k, v in di.items():
            lol.append(v)
        return lol