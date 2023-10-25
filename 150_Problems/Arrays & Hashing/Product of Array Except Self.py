# Medium
# https://leetcode.com/problems/product-of-array-except-self/description/

#############
# Solution: 1
#############
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d, prd, zero = {}, 1, 0
        for idx, val in enumerate(nums):
            if val != 0:
                prd = val*prd 
            else:
                zero += 1
            d[idx] = val
        
        if zero > 1:
            return [0]*len(nums)
        else:
            new_nums = []
            for k, v in d.items():
                if zero == 1 and v != 0:
                    new_nums.append(0)
                elif zero == 1 and v == 0:
                    new_nums.append(prd)
                else:
                    new_nums.append(int(prd/v))
        return new_nums

#Runtime 196 ms Beats 51.24%
#Memory 27.9 MB Beats 7.5%
####################################################
# Solution: 2
#############
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre, post = 1, 1
        rslt = [1]*l
        
        for i in range(l):
            rslt[i] = pre
            pre *= nums[i]
            
        for j in range(l):
            rslt[l-j-1] *= post
            post *= nums[l-1-j]
        
        return rslt
#Runtime 203 ms Beats 28.36%
#Memory 24.07 MB Beats 53.37%
####################################################
# Solution: 3
#############
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre, post = 1, 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return sol
#Runtime 186 ms Beats 85.62%
#Memory 23.89 MB Beats 74.67%