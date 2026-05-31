class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        st = []
        for x in s:
            if x in d.keys():
                st.append(x)
            else:
                if st and d[st[-1]] == x:
                    st.pop()
                else:
                    return False
        return len(st) == 0    