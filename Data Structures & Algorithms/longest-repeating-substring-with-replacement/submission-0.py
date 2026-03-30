class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            a, b = i, i+1
            ch = s[a]
            k1 = k
            while b<len(s):
                if ch == s[b]:
                    b+=1
                else:
                    if k1>0:
                        b+=1
                        k1-=1
                    else:
                        break
            res = max(res, b-a)
        return res