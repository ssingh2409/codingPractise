# https://leetcode.com/problems/container-with-most-water/description/

#############
# Solution: 1 (FAILED)
#############
class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        for k1, v1 in enumerate(height):
            for k2, v2 in enumerate(height[k1+1:]):
                mx = max(min(v1, v2)*(k2+1), mx)
                
        return mx

#Brute Force, did not finish - 51/62
#########################################################
# Solution: 2
#############
class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        numHash = {}
        for k,v in enumerate(height):
            numHash[k]=v
            e = k
		
        s, l = 0, e

        while s<e:
            mx = max(min(numHash[s], numHash[e]) * l, mx)
            if (numHash[s] > numHash[e]):
                e-= 1
            else:
                s+= 1
            l-= 1
        return mx

#Runtime 578 ms Beats 5.04%
#Memory 34.68 MB Beats 6.91%
#########################################################
# Solution: 3 - same as 2 but without use of dict
#############
class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        s, e = 0, len(height)-1

        while s<e:
            mx = max(min(height[s], height[e]) * (e-s), mx)
            if (height[s] > height[e]):
                e-= 1
            else:
                s+= 1
        return mx

#Runtime 534 ms Beats 34.87%
#Memory 29.38 MB Beats 84.52%