# https://leetcode.com/problems/two-sum/description/

#############
# Solution: 1
#############
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num_to_check = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == num_to_check:
                    return [i, j]

# Runtime 1450 ms Beats 36.61%
# Memory 17.1 MB Beats 82.31%

#################################################################
# Solution: 2
#############
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        l = len(nums)

        for i in range(l):
            num_to_check = target - nums[i]
            if num_to_check in numHash:
                return[i, numHash[num_to_check]]
            numHash[nums[i]] = i

#Runtime 69 ms Beats 52.47%
#Memory 17.5 MB Beats 41.05%
#################################################################
# Solution: 3
#############
