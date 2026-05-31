class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = []
        for x in operations:
            if x == "+":
                a = li[-1] + li[-2]
                li.append(a)
            elif x == 'D':
                a = li[-1] * 2
                li.append(a)
            elif x == 'C':
                li.pop()
            else:
                li.append(int(x))
        return sum(li)