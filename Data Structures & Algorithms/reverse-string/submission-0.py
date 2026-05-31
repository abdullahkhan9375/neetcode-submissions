class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            x = s[i]
            y = s[j]
            tmp = x
            s[i] = y
            s[j] = tmp
            i += 1
            j -= 1
