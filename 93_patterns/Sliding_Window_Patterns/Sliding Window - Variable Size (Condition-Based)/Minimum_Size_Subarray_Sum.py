# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3] Output: 2 Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4] Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1] Output: 0

# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         subarray = []
#         min_len = len(nums)
#         curr_sum = 0
#         sol = 0

#         for i in nums:
#             subarray.append(i)
#             curr_sum += i
#             print(subarray, curr_sum)
                
#             while curr_sum >= target:
#                 if curr_sum == target: 
#                     min_len = min(min_len, len(subarray))
#                     sol += 1

#                 out = subarray.pop(0)
#                 curr_sum -= out
#                 print('post', subarray, curr_sum, min_len)

#         return min_len if sol > 0 else 0
    

class Solution(object):
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        start = 0
        sum = 0
        min_size = float("inf")
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1

        return min_size if min_size != float("inf") else 0

# Time:  O(nlogn)
# Space: O(n)
# Binary search solution.

a = Solution()
print(a.minSubArrayLen(7, [2,3,1,2,4,3]))
