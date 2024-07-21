class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_char = {}
        count = 0
        begin = 0

        for end in range(len(s)):
            if s[end] in index_char:
                begin = max(begin, index_char[s[end]] + 1)
            
            index_char[s[end]] = end

            count = max(count, end - begin + 1)
        
        return count
        
