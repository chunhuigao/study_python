


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # type: ignore
        ll = []
        d = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in d:
                d[ss] = []
            d[ss].append(s)
        for v in d.values():
            ll.append(v)
        return ll

result = Solution()
r = result.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(r)