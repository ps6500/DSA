"""

Longest Substring Without Repeating Characters

Given a string s having lowercase characters, find the length of the longest substring without repeating characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7 
Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.

Input: s = "aaa"
Output: 1
Explanation: The longest substring without repeating characters is "a"

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring without repeating characters is "abcdef".

"""

def length_of_longest_substring(s: str) -> int:
    # Dictionary to store last index of each character
    last_idx = {}

    max_len = 0
    start = 0  # left boundary of current window

    for i, ch in enumerate(s):
        # If character seen and is inside current window, move start
        if ch in last_idx and last_idx[ch] >= start:
            start = last_idx[ch] + 1

        # Update max length for window [start, i]
        curr_len = i - start + 1
        if curr_len > max_len:
            max_len = curr_len

        # Update last seen index of current character
        last_idx[ch] = i

    return max_len



if __name__ == "__main__":
    s = "geeksforgeeks"
    print(length_of_longest_substring(s))
