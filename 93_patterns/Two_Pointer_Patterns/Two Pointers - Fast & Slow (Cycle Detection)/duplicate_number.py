# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2] Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2] Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3] Output: 3

# Constraints:
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
def duplicatenumber(nums):
    i = 0

    slow = i
    fast = i+1

    while True:
        print(slow, fast)
        if nums[slow] == nums[fast]: break
        if slow < len(nums)-1:
            slow+=1
        if fast == len(nums)-1 or fast == len(nums)-2:
            fast = 0
        else:
            fast+=2

    return nums[slow]

print(duplicatenumber([9, 8, 7, 6, 5, 4, 3, 2, 1, 9]))
