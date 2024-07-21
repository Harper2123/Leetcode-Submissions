class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            return s == s[::-1]
        
        max_len = 0
        long_palin = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                subs = s[i:j+1]

                if isPalindrome(subs) and len(subs) > max_len:
                    max_len = len(subs)
                    long_palin = subs
        
        return long_palin
