# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1 Output: 2 Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1 Output: 0 Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

def threeSumClosest(nums, target):
    nums.sort()
    i = 0
    result = {}
    while i <(len(nums)-2):
        num1 = nums[i]
        left, right = i+1, len(nums)-1
        
        while left < right:
            num2 = nums[left]
            num3 = nums[right]
            
            curr_sum = num1 + num2 + num3
            diff = target - curr_sum
            result[diff] = curr_sum

            if diff == 0: return curr_sum
            elif curr_sum > target: right -= 1
            else: left += 1
        
        i+=1
    min_val = min(result.keys())
    return result[min_val]

print(threeSumClosest([-1,2,1,-4], 1))
# print(threeSumClosest([0,0,0], 1))