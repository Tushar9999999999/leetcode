class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        a = list(d.values())
        a.sort(reverse=True)
        re = []
        b = 0
        while k > 0:
            for key, value in d.items():
                if a[b] == value:
                    re.append(key)
            b+=1
            k-=1
        return re