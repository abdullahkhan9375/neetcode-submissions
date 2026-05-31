class Solution:
    def sq(self, n):
        s = str(n)
        su = 0
        for x in s:
            su += int(x) ** 2
        return su

    def isHappy(self, n: int) -> bool:
        seen = {}
        while n not in seen:
            seen[n] = 0
            n = self.sq(n)
            if n == 1:
                return True
        return False
        