class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        s = sorted(count.items(), key = lambda item: item[1])
        res = []
        while k > 0:
            res.append(s.pop()[0])
            k -= 1
        return res

