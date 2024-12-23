class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_of_given_string = len(s)
        max_length = 0
        char_index = [-1] * 128
        left = 0
        for right in range(length_of_given_string):
            if char_index[ord(s[right])] >= left:
                left = char_index[ord(s[right])] + 1
            char_index[ord(s[right])] = right
            max_length = max(max_length, right - left + 1)
        return max_length