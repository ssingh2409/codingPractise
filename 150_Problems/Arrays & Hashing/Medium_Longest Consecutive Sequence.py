# https://leetcode.com/problems/longest-consecutive-sequence/description/

#############
# Solution: 1
#############
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums.sort()
        mx_seq, runn_seq = 0, 0

        for i in nums:
            if runn_seq == 0: runn_seq = 1
            else:
                if i == nxt:
                    runn_seq += 1
                elif i == prev: continue
                else: runn_seq = 1
            prev = i
            nxt = i + 1
            mx_seq = max(mx_seq, runn_seq)
            print(i, runn_seq, mx_seq)
        return mx_seq

#Runtime 588 ms Beats 38.51%
#Memory 30.86 MB Beats 91.91%
#################################################################
# Solution: 2
#############
