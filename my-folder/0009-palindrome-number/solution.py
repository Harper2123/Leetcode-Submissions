class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            rev = 0
            start = x
            while x != 0:
                rev = (rev*10) + x % 10
                x = x // 10
            if(rev == start):
                return True
            return False
