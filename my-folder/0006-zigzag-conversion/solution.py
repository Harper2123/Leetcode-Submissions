class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        current = 0
        going_down = False

        for char in s:
            rows[current] += char

            if current == 0 or current == numRows - 1:
                going_down = not going_down
            if going_down:
                current += 1
            else:
                current -= 1
        
        return "".join(rows)
        
