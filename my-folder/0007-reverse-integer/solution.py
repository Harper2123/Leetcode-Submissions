class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if y[0] == '-':
            y_tab = int('-' + y[1:][::-1])
            if y_tab < (-1*2**31) or y_tab > (2**31 - 1):
                return 0
            else:
                return y_tab
        
        else:
            y_tab = int(y[::-1])
            if y_tab < (-1*2**31) or y_tab > (2**31 - 1):
                return 0
            else:
                return y_tab
        
