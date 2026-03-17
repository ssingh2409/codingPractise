# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [9,4] Explanation: [4,9] is also accepted.

 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    rslt = []
    left, right = 0, 0

    while left <= len(nums1)-1 and right <= len(nums2)-1:
        if nums1[left] == nums2[right]:
            rslt.append(nums1[left])
            left+= 1
            right+=1
        elif nums1[left] < nums2[right]: left+= 1
        else: right+= 1

        if left < len(nums1)-1: 
            if nums1[left] == nums1[left+1]: left+= 1 
        if right < len(nums2)-1: 
            if nums2[right] == nums2[right+1]:right+= 1
                
    return rslt

print(intersection([4,9,5], [9,4,9,8,4]))