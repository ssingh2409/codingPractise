# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0 Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [2,2,2,2,2], target = 8 Output: [[2,2,2,2]]

 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

def fourSums(nums, target):
    nums.sort()
    print(nums)
    i = 0
    result = []

    while i < len(nums)-3:
        j = i + 1
        while j < len(nums)-2:
            left, right = j + 1, len(nums)-1

            while left < right:
                print(nums[i], nums[j], nums[left], nums[right])
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if curr_sum == target: 
                    if [nums[i], nums[j], nums[left], nums[right]] not in result: result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                elif curr_sum < target: left += 1
                else: right -= 1
            j += 1
        i += 1
    return result

print(fourSums([2,2,2,2,2], 8))