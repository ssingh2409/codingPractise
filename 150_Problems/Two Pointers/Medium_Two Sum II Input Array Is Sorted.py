# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

#############
# Solution: 1
#############
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        strt, end = 0, len(nums)-1

        while strt < end:
            curr_sum = nums[strt] + nums[end]
            if curr_sum == target: return [strt+1, end+1]
            if curr_sum < target: strt+= 1
            if curr_sum > target: end-= 1

        return False

#Runtime 111 ms Beats 91.66%
#Memory 17.13 MB Beats 66.41%
#########################################################
# Solution: 2
#############
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numHash = {}

        for i, v in enumerate(numbers):
            if numHash.get(target-v, False):
                return [numHash[target-v], i+1]
            else:
                numHash[v]=i+1

#Runtime 127 ms Beats 18.95%
#Memory 17.22 MB Beats 26.99%