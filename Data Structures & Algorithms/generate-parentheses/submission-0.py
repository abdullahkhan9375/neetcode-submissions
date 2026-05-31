class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back_track(openN, closedN, path):
            if openN == closedN == n:
                res.append(path)
                return
            
            if openN < n:
                back_track(openN + 1, closedN, path + "(")
            
            if closedN < openN:
                back_track(openN, closedN + 1, path + ")")
            
        
        back_track(0, 0, "")
        return res