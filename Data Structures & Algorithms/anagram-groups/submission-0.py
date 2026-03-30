class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)
        for i in strs:
            a = "".join(sorted(i))
            d[a].append(i)
        for key, values in d.items():
            res.append(values)
        return res
            