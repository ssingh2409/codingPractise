# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c" Output: true Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#" Output: true Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b" Output: false Explanation: s becomes "c" while t becomes "b".

# class Solution: # AI Solution
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         p1, p2 = len(s)-1, len(t)-1
#         while p1 >= 0 or p2 >= 0:
#             back_s = back_t = 0
#             while p1 >= 0 and (s[p1] == '#' or back_s > 0):
#                 if s[p1] == '#': back_s += 1
#                 else: back_s -= 1
#                 p1 -= 1
            
#             while p2 >= 0 and (t[p2] == '#' or back_t > 0):
#                 if t[p2] == '#': back_t += 1
#                 else: back_t -= 1
#                 p2 -= 1
            
#             if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]: return False
#             if (p1 >= 0) != (p2 >= 0): return False
            
#             p1 -= 1
#             p2 -= 1
        
#         return True


# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s_list, t_list = [], []
#         p1, p2 = 0, 0
#         while True:
#             if p1 < len(s):
#                 if s[p1] == '#': 
#                     if s_list: s_list.pop()
#                 else: s_list.append(s[p1])
            
#             if p2 < len(t):
#                 if t[p2] == '#': 
#                     if t_list: t_list.pop()
#                 else: t_list.append(t[p2])
#             # print(s_list, t_list)
#             p1+=1
#             p2+=1

#             if p1 >= len(s) and p2 >= len(t): break
        
#         return True if s_list == t_list else False
    

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s)-1
        p2 = len(t)-1

        while p1 >= 0 or p2>= 0:
            hash_s = hash_t = 0
            while p1>=0 and (s[p1]=='#' or hash_s > 0):
                if s[p1]=='#': hash_s += 1
                else: hash_s -= 1
                p1 -=1

            while p2>=0 and (t[p2]=='#' or hash_t > 0):
                if t[p2]=='#': hash_t += 1
                else: hash_t -= 1
                p2 -= 1
            
            # print(p1, p2)
            if p1 < 0 and p2 < 0 : break
            # print(s[p1], t[p2])
            if s[p1] != t[p2]: return False
            
            p1 -= 1
            p2 -= 1

        return True
           



sol = Solution()
print(sol.backspaceCompare('ab#c', 'ad#c'))
print(sol.backspaceCompare('ab##', 'c#d#'))
print(sol.backspaceCompare('a#c', 'b'))
print(sol.backspaceCompare('####', '#'))
print(sol.backspaceCompare('xy##z#w#v##', 'z#w#'))

