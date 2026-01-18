# You are given a 0-indexed integer array nums and an integer k.
# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
# You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
# Return the maximum score you can get.

 

# Example 1:
# Input: nums = [1,-1,-2,4,-7,3], k = 2 Output: 7 Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

# Example 2:
# Input: nums = [10,-5,-2,4,0,3], k = 3 Output: 17 Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

# Example 3:
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2 Output: 0

# Constraints:
# 1 <= nums.length, k <= 105
# -104 <= nums[i] <= 104



# class Solution(object):
#     def maxResult(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         final_sum = nums[0]
#         i = 0
#         while True:
#             if i == len(nums)-1:
#                 break
#             print('jumping from :',i)
#             temp_largest = nums[i+1]
#             for x in range(i+1, min(i+k+1, len(nums))):
#                 pntr = i+1
#                 if nums[x] > temp_largest: 
#                     print('found a larger number')
#                     pntr=x
#                     temp_largest = nums[x]
#                 print(x, nums[x], 'curr-highest', temp_largest)
#             i = max(i+1, pntr)
#             final_sum += temp_largest
#             print('total is: ', final_sum)
            
#         return final_sum

# import collections
# class Solution(object):
#     def maxResult(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         score = 0
#         dq = collections.deque()
#         for i, num in enumerate(nums):
#             print(i, num)
#             if dq and dq[0][0] == i-k-1:
#                 dq.popleft()
#             score = num if not dq else dq[0][1]+num
#             print(score)
#             while dq and dq[-1][1] <= score:
#                 dq.pop()
#             dq.append((i, score))
#             print(dq)
#         return score


class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        final_score = 0
        temp_list = []
        for i, val in enumerate(nums):
            if temp_list and temp_list[0][0] == i-k-1:
                temp_list.pop(0)
            final_score = val if not temp_list else temp_list[0][1]+val
            while temp_list and temp_list[-1][1] <= final_score:
                print('pop')
                temp_list.pop(-1)
            temp_list.append((i, final_score))
            print(temp_list)



a = Solution()
# print(a.maxResult([-1, -2, -3, -4, -5], 2))
print(a.maxResult([1,-1,-2,4,-7,3], 2))