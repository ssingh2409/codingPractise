# Easy
# https://leetcode.com/problems/valid-anagram/description/

#############
# Solution: 1
#############
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}

        for i in s:
            dict_s[i] = dict_s.get(i, 0) +1
        
        for j in t:
            dict_t[j] = dict_t.get(j, 0) +1

        return True if dict_s == dict_t else False

# Runtime 54 ms Beats 59.33%
# Memory 16.8 MB Beats 72.80%

#################################################################
# Solution: 2
#############
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return True if s == t else False

#Runtime 51 ms Beats 72.72%		
#Memory 17.6 MB Beats 9.50%

#################################################################
# Solution: 3
#############
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = {}

        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i], 0) + 1
            cnt[t[i]] = cnt.get(t[i], 0) - 1

        for v in cnt.values():
            if v != 0:
                return False
        return True
#Runtime 64 ms Beats 13.50%
#Memory 16.8 MB Beats 72.80%