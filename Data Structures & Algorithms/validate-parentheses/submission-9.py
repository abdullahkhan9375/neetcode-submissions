class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        st = []
        for x in s:
            if x == "(":
                st.append(x)
            elif x == "{":
                st.append(x)
            elif x == "[":
                st.append(x)
            elif x == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False
            elif x == "}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    return False
            else:
                if st and st[-1] == "[":
                    st.pop()
                else:
                    return False
        return len(st) == 0

        
        return len(st) == 0
                