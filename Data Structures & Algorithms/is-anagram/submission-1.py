class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t1 = t
        for i in s:
            if i in t1:
                t1 = t1.replace(i, "", 1)
                print(t1)
            else:
                return False
        if t1 == "":
            return True
        return False
            