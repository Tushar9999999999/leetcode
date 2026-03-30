class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        res = []
        for i, a in enumerate(n):
            if i>0 and a == n[i-1]:
                continue

            l, r  = i, len(nums)-1
            while l<r:
                temp = a + n[l] + n[r]
                if temp > 0:
                    r-=1
                elif temp < 0:
                    l+=1
                else:
                    res.append([a, n[l], n[r]])
                    l+=1
                    r-=1
                    while n[l] == n[l-1] and l<r:
                        l+=1
        return res
            