# https://leetcode.com/problems/valid-palindrome/description/

#############
# Solution: 1
#############
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        fr, bk = 0, l-1

        while bk >= fr:
            if not s[fr].lower().isalnum():
                fr += 1
                continue
            if not s[bk].lower().isalnum():
                bk -= 1
                continue
            if s[fr].lower() != s[bk].lower():
                return False
            fr += 1
            bk -= 1
            
        return True
		
# Runtime 58 Beats 23.63%
# Memory 16.98MB Beats 90.86%

#################################################################
# Solution: 2
#############
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for c in s.lower():
            if c.isalnum():
                s1 += c

        return True if s1==s1[::-1] else False
		
# Runtime 43 ms Beats 87.29%
# Memory 17.08MB Beats 69.6%

#################################################################
# Solution: 3
#############
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))

# Runtime 27 ms Beats 99.96%
# Memory 22.22 MB Beats 9.65%