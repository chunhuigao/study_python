class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ll = [0] * 128
        for c in t:
            ll[ord(c)] += 1
        # 无重复字符串长度
        slen = 0
        for c in ll:
           
            if c > 0:
                slen += 1
        currentLen = 0
        left = 0
        start = 0
        min_len = 10000000000
        for i in range(len(s)):
            ss = s[i]
            ll[ord(ss)] -= 1
            if ll[ord(ss)] == 0:
                currentLen += 1
            # 当当前字符串长度为无重复字符串长度时，说明当前字符串为最小字符串
            while left <= i and currentLen == slen:
                if i - left + 1 < min_len:
                    min_len = i - left + 1
                    start = left
                ll[ord(s[left])] += 1
                if ll[ord(s[left])] > 0:
                    currentLen -= 1
                left += 1
        return '' if min_len == 0 else s[start:start+min_len]
    
result = Solution().minWindow("ADOBECODEBANC","ABC")
print(result)
        

