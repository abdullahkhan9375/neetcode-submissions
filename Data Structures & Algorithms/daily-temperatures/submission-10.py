class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        dist = []
        flag = False
        for i in range(len(temp)):
            flag = False
            for j in range(i + 1, len(temp)):
                x = temp[i]
                y = temp[j]
                if (y > x):
                    dist.append(j - i)
                    flag = True
                    break

            if not flag:
                dist.append(0)
                flag = False
        return dist
