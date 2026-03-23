"""

1763. Longest Nice Substring
Easy
Topics
premium lock icon
Companies
Hint
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.

"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        # Use a set for O(1) average time complexity lookups
        char_set = set(s)

        for i, char in enumerate(s):
            # Check if both cases of the current character are present in the *current* string
            if char.lower() in char_set and char.upper() in char_set:
                continue
            
            # If not, the current string is not nice, and the longest nice substring 
            # must be entirely within the left or right partition
            sub1 = self.longestNiceSubstring(s[:i])
            sub2 = self.longestNiceSubstring(s[i+1:])
            print(sub1)
            print(sub2)
            # Return the longer of the two resulting nice substrings
            return sub1 if len(sub1) >= len(sub2) else sub2

        # If the loop finishes, the entire string 's' is nice
        return s



if __name__ == '__main__':
    s = "YazaAay"
    solver = Solution()
    print(solver.longestNiceSubstring(s))
