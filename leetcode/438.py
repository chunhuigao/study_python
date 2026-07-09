from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plist = [0]*26
        for pp in p:
            idx = ord(pp)-97
            plist[idx]+=1
        target = ','.join(map(str, plist))
        slist = [0] *26
        res = []
        for i in range(len(s)):
            ss = s[i]
            idx = ord(ss)-97
            slist[idx]+=1
            if i >= len(p):
                ii = ord(s[i-len(p)]) - 97
                slist[ii]-=1
            starget = ','.join(map(str, slist))
            if starget == target:
                res.append(i-len(p)+1)
     
        return res
    
result = Solution().findAnagrams("cbaebabacd","abc")
result2 = Solution().findAnagrams("abab","ab")
print(result,result2)