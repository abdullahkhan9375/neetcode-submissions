class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for x in nums:
            if x in di.keys():
                di[x] = di[x] + 1
            else:
                di[x] = 1
        
        l = []
        di = {k: v for k, v in sorted(di.items(), key=lambda item: item[1], reverse=True)}
        di = list(di.keys())
        for i in range(k):
            l.append(di[i])
        return l