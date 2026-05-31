class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = [x.lower() for x in s if x.isalnum()]
        print(s)
        idx1 = 0
        idx2 = len(s) - 1
        if not s:
            return True
        while idx1 != idx2:
            print(idx1, idx2)
            l = s[idx1]
            l2 = s[idx2]
            if l != l2:
                return False
            idx1 += 1
            idx2 -= 1
            if (idx1 > len(s) - 1):
                break
            elif (idx2 < 0):
                break
        return True
