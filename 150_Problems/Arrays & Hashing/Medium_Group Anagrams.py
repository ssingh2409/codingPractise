# https://leetcode.com/problems/group-anagrams/description/

#############
# Solution: 1
#############
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}

        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in str_dict:
                str_dict[sorted_str].append(i)
            else:
                str_dict[sorted_str] = [i]
        
        return list(str_dict.values())

#Runtime 92 ms Beats 85.33%
#Memory 19.5 MB Beats 89.8%