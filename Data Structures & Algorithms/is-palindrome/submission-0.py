class Solution:
    def isPalindrome(self, s: str) -> bool:
        A = []
        for i in s:
            if i.isalnum():
                A.append(i.lower()) 
        B = list(reversed(A))
        if A == B:
            return True
        else:
            return False