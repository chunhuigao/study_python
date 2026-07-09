class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ''
        ll = 0
        for i in range(len(s)):
            if s[i] in temp:
                temp = temp[temp.index(s[i])+1:]
            temp += s[i]
            ll = max(ll,len(temp))
        return ll
    
result = Solution().lengthOfLongestSubstring("abcabcbb")
print(result)