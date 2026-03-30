class Solution:
    def isPalindrome(self, s: str) -> bool:
        a, b = 0, len(s)-1
        while a<b:
            if s[a].isalnum():
                if s[b].isalnum():
                    if s[a].lower() == s[b].lower():
                        a += 1
                        b -= 1
                    else:
                        return False
                else:
                    b -= 1
            else:
                a+=1
        return True