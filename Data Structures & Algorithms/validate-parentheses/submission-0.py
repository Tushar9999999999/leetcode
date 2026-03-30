class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                st.append(i)
            if i == "}":
                if st.pop() != "{":
                    return False
            if i == ")":
                if st.pop() != "(":
                    return False
            if i == "]":
                if st.pop() != "[":
                    return False
        if st == []:
            return True
        else:
            return False
            
            
