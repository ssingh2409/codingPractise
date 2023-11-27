# https://leetcode.com/problems/3sum/description/

#############
# Solution: 1 (FAILED)
#############
def threeSums(nums):
    l = len(nums)
    if l < 3: return []

    nums_dict = {}
    for k, v in enumerate(nums):
        nums_dict[k] = v
    
    final_list = set()   
    
    for i in range(l-2):
        a = nums_dict[i]
        for j in range(i+1, l-1):
            b = nums_dict[j]
            for k in range(j+1, l):
                c = nums_dict[k]
#                 print(a,b,c)
                if a+b+c == 0:
                    temp = [a,b,c]
                    temp.sort()
                    print(temp)
                    final_list.add((temp))
    
    return final_list

#FAILED - 308/312 - Time limit exceeded
#########################################################
# Solution: 2
#############
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        if l < 3: return []

        nums_dict = {}
        for k, v in enumerate(nums):
            nums_dict[k] = v

        final_set = set()    

        for i in range(l-2):
            j, k = i+1, l-1
            while j < k:
                s = nums_dict[i] + nums_dict[j] + nums_dict[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    final_set.add((nums_dict[i], nums_dict[j], nums_dict[k]))
                    j += 1
                    k -= 1
            
        return final_set

#Runtime 2494 ms Beats 20.18%
#Memory 20.62 MB Beats 27.96%