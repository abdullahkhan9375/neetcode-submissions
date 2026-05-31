class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0 for x in temperatures]

        con = 0
        stack = []
        ptr1 = 0
        ptr2 = 1
        while ptr1 < len(temperatures) - 1:
            l1 = temperatures[ptr1]
            l2 = temperatures[ptr2]
            if l1 < l2:
                arr[ptr1] = ptr2 - ptr1
                ptr1 += 1
                ptr2 = ptr1
            else:
                ptr2 += 1
            if ptr2 >= len(temperatures):
                ptr1 += 1
                ptr2 = ptr1
        return arr

