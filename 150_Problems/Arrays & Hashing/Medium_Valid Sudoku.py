# https://leetcode.com/problems/valid-sudoku/description/

#############
# Solution: 1
#############
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict, col_dict, cubes = {}, {}, {}
        for r, lst in enumerate(board):
            for c, elem in enumerate(lst):

                #Create ROW
                if r in row_dict:
                    if elem in row_dict[r] and elem != '.':
                        return False 
                    else: row_dict[r].append(elem)
                else: row_dict[r] = [elem]

                # Create COLUMNS
                if c in col_dict:
                    if elem in col_dict[c] and elem != '.':
                        return False 
                    else: col_dict[c].append(elem)
                else: col_dict[c] = [elem]

                #Create 3x3 matrix
                cube_num = str(r//3)+ str(c//3)
                if cube_num in cubes:
                    if elem in cubes[cube_num] and elem != '.':
                        return False 
                    else: cubes[cube_num].append(elem)
                else: cubes[cube_num] = [elem]
        return True

#Runtime 117 ms Beats 6.13%
#Memory 16.2 MB Beats 85.43%
#################################################################
# Solution: 2
#############
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != '.':
                    res += ([(i, val), (val, j), (i // 3, j // 3, val)])
        return len(res) == len(set(res))

#Runtime 89 ms Beats 98.16%
#Memory 16.16 MB Beats 85.43%