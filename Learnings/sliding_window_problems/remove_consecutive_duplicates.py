"""

Remove all consecutive duplicates from a string

Given a string s , we have to remove all the consecutive duplicate characters of the string and return the resultant string. 

Examples: 

Input: str = "aaaaabbbbbb"
Output: ab
Explanation: Remove consecutive duplicate characters from a string s  such as 5 a's are at consecutive so only write a and same like that in b's condition.

Input: str = "geeksforgeeks"
Output: geksforgeks
Explanation: Remove consecutive duplicate characters from "geeksforgeeks", so "ee" becomes "e", resulting in "geksforgeks"

"""


def remove_consecutive_duplicates(s: str) -> str:
    """
    Remove all consecutive duplicate characters from string.
    
    Time: O(n)  - Single pass through string
    Space: O(n) - Result list in worst case
    """
    if not s:
        return s
        
    result = []
    for char in s:
        # Only add char if it's different from last char in result
        if not result or char != result[-1]:
            result.append(char)
    
    return ''.join(result)


#alternative Solution
import re
def remove_duplicates(str):
    # Create a regex pattern to match consecutive duplicate characters
    return re.sub(r'(.)\1+', r'\1', str)

if __name__ == "__main__":
    str = "geeksforgeeks"
    print(remove_consecutive_duplicates(str))  # Output: "geksforgeks"



