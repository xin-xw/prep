"""
@understand
input: Given matrix board: List[List[String]], where it's only valid if the following rules are followed:
1. Each row much contain the digists 1-9 without duplicates
2. Each column must contain the digits 1-9 without duplicates
3. Each of the 9, 3x3 sub-boxes of the grid must contain the digits 1-9 without duplicates

output: boolean: True if board is Valid/False otherwise

@match

Q: If we are ensuring 1/2 remains True, then that's easy because we can brute-force check it with two boolean Flags that return False if conditions violate. How can we also ensure if 3 is also True? 

* 9 Rows -> Each number can only be used once in every row
* 9 Cols -> Each number can only be used once in every col
* Using 1 number at any given spot, deems it invalid to be used for both specific row and col

/naive

* Check every row for repeated digits, check every col. for repeated digits; the below are fixed
After checking the first 2 conditions, we can check each sub-box and verify repeated digits
- rows 012 cols 012 belong to box 1
- rows 012 cols 345 belong to box 2
- rows 012 cols 678 belong to box 3
- rows 345 cols 012 belong to box 4
- rows 345 cols 345 belong to box 5
- rows 345 cols 678 belong to box 6
- rows 678 cols 012 belong to box 7
- rows 678 cols 345 belong to box 8
- rows 678 cols 678 belong to box 9

* Sets in Python allow us to verify repeated values quickly 
    * main function provide subfunction a subgroup to check validity
        * 9 sub-boxes
        * 9 rows
        * 9 cols
    * subfunction is_valid_subgroup will validate return boolean 
        1. declare a set
        2. loop through the subgroup 
            3. if value is a "." -> ignore
            4. else, check if value is in set or not -> return F if it is
            5. add value to set
        6. return T for valid subgroup 

"""

class Solution:
    def is_valid_subgroup(self, subgroup: List[str]) -> bool: 
        seen = set()

        for value in subgroup:
            if value == ".":
                continue
            if value in seen:
                return False
            seen.add(value)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)    # Number of rows
        cols = len(board[0]) # Number of cells in the first row = columns
        res = []
        for row in range(rows):
            res.append(self.is_valid_subgroup(board[row]))

        # To access column, we are iterating row by row first, then the actual column next
        """
        col 0: (0, 0), (1, 0), (2, 0), ...
        col 1: (1, 0), (1, 1), (2, 1), ...
        """
        
        for col in range(cols):
            column = []
            for row in range(rows):
                column.append(board[row][col])
            res.append(self.is_valid_subgroup(column))

        boxes = {}

        """
        As we loop through each row and col, each cell separates into 3 groups: 
        1) If we judge by col, each cell separates into 3 groups left/mid/right if we do col//3.
        2) If we judge by row, each cell separates into 3 groups top/mid/bot if we do row//3.
        
        0//3 = 0 -> Group 0
        1//3 = 0
        2//3 = 0

        3//3 = 1 -> Group 1
        4//3 = 1
        5//3 = 1

        6//3 = 2 -> Group 2
        7//3 = 2
        8//3 = 2

        cell (7,4) -> box(2,1) -> bottom middle box
        """

        for row in range(rows):
            for col in range(cols):
                box = (row//3, col//3)
                if box not in boxes:
                    boxes[box] = []
                boxes[box].append(board[row][col])

        for key, values in boxes.items():
            print(values)
            res.append(self.is_valid_subgroup(values))

        return all(res)


