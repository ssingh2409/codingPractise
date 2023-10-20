# Easy
# https://leetcode.com/problems/contains-duplicate/description/

#############
# Solution: 1
#############

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_l = set(nums)
        return False if len(new_l) == len(nums) else True
		
# Runtime 465ms Beats 86.98%
# Memory 31.8MB Beats 38.4%

#################################################################
# Solution: 2
#############
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
		
#Runtime 486ms Beats 32.83%
#Memory 30.84MB Beats 73.59%

#################################################################
# Solution: 3
#############
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elem = {}
        ret = False

        for i in nums:
            if i in elem:
                elem[i] += 1
                ret = True
            else:
                elem[i] = 1
        
        return ret
#Runtime 516 ms Beats 8.75%
#Memory 33.5 MB Beats 17.98%