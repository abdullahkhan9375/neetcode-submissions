class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def rec(stones):
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 2:
                if stones[0] == stones[1]:
                    return 0
            stones_sorted = sorted(stones)
            l, r = stones_sorted[len(stones) - 2], stones_sorted[len(stones) - 1]
            if l == r:
                stones_sorted = stones_sorted[0:-2]
            else:
                stones_sorted = stones_sorted[0:-1]
                stones_sorted[-1] = abs(l - r)
            print(stones_sorted)
            return rec(stones_sorted)
        return rec(stones)
