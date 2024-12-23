#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {
    int length_of_given_string = strlen(s);
    int max_length = 0;
    int char_index[128];
    memset(char_index, -1, sizeof(char_index));
    int left = 0;
    for (int right = 0; right < length_of_given_string; right++) {
        if (char_index[s[right]] >= left) {
            left = char_index[s[right]] + 1;
        }
        char_index[s[right]] = right;
        max_length = (max_length > right - left + 1) ? max_length : right - left + 1;
    }
    return max_length;
}

int main() {
    char s[] = "abcabcbb";
    printf("Length of longest substring without repeating characters: %d\n", lengthOfLongestSubstring(s));
    return 0;
}