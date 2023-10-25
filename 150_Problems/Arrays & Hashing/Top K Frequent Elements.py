# Medium
# https://leetcode.com/problems/top-k-frequent-elements/description/

#############
# Solution: 1
#############
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict, mx = {}, []
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        
        l = list(dict.values())
        l.sort(reverse=True)

        l = l[:k]

        for i in l:
            num = [key for key, val in dict.items() if (val == i) and (key not in mx)][0]
            mx.append(num)
        
        return mx

# Runtime 50 ms Beats 5.00%
# Memory 20.77 MB Beats 97.8%

#################################################################
# Solution: 2
#############
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        return sorted(d, key=d.get, reverse=True)[:k]
# Runtime 89 ms Beats 93.8%
# Memory 20.96 MB Beats 75.51%
#################################################################
# Solution: 3
#############
