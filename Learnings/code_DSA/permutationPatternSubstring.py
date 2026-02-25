"""

Given two strings txt and pat having lowercase letters, the task is to check if any permutation of pat is a substring of txt.

Examples:

Input: txt = "geeks", pat = "eke"
Output: true
Explanation: "eek" is a permutation of "eke" which exists in "geeks".

Input: txt = "programming", pat = "rain"
Output: false
Explanation: No permutation of "rain" exists as a substring in "programming".

"""

"""

# Python Program to check if any permutation of pattern
# is substring by checking all possible substrings

MAX_CHAR = 26

def arePermutations(txt, startIdx, pat):
    freq = [0] * MAX_CHAR
    for i in range(len(pat)):

        # Increment the count of character in txt
        freq[ord(txt[startIdx + i]) - ord('a')] += 1

        # Decrement the count of character in pat
        freq[ord(pat[i]) - ord('a')] -= 1

    for i in range(MAX_CHAR):
        if freq[i] != 0:
            return False
    return True

def search(txt, pat):
    n = len(txt)
    m = len(pat)

    for i in range(n - m + 1):

        # Check if substring in txt starting from i
        # is a permutation of pat
        if arePermutations(txt, i, pat):
            return True

    return False

if __name__ == "__main__":
    txt = "geeks"
    pat = "eke"
    if search(txt, pat):
        print("true")
    else:
        print("false")





# Python Program to check if any permutation of string
# is substring using Sliding Window Technique

MAX_CHAR = 26

# check if all characters have 0 frequency
def check(freq):
    for i in range(MAX_CHAR):
        if freq[i] != 0:
            return False
    return True

def search(txt, pat):
    n = len(txt)
    m = len(pat)

    # construct the first window
    freq = [0] * MAX_CHAR
    for i in range(m):
        freq[ord(txt[i]) - ord('a')] += 1
        freq[ord(pat[i]) - ord('a')] -= 1

    # Check for first window
    if check(freq):
        return True

    for i in range(m, n):

        # Add the ith character into the window
        freq[ord(txt[i]) - ord('a')] += 1

        # Remove the (i - m)th character from the window
        freq[ord(txt[i - m]) - ord('a')] -= 1

        # Check for the current window
        if check(freq):
            return True

    return False

"""

from collections import Counter

def check_permutation_substring(txt: str, pat: str) -> bool:
    if len(pat) > len(txt): return False  # Quick fail
    
    pat_count = Counter(pat)              # Target: {'e':2,'k':1}
    required = len(pat_count)             # Must match ALL 3 chars
    window_count = Counter()
    matches = 0                           # How many chars match exactly?

    print("====================== checkpoint 1 =======================")
    print("pat_count = "+str(pat_count))
    print("required = "+str(required))
    print("window_count = "+str(window_count))
    print("matches = "+str(matches))
    print("====================== checkpoint 1 =======================")    
    
    # Step 1: Fill first window
    for i in range(len(pat)):
        window_count[txt[i]] += 1
        if window_count[txt[i]] == pat_count[txt[i]]:
            matches += 1                    # This char now perfect!
    
    print("====================== checkpoint 2 =======================")
    print("pat_count = "+str(pat_count))
    print("required = "+str(required))
    print("window_count = "+str(window_count))
    print("matches = "+str(matches))
    print("====================== checkpoint 2 =======================")

    if matches == required: return True   # First window perfect?
    
    # Step 2: Slide window
    for i in range(len(pat), len(txt)):
        
        print("====================== checkpoint 3 =======================")
        print("pat_count = "+str(pat_count))
        print("required = "+str(required))
        print("window_count = "+str(window_count))
        print("matches = "+str(matches))
        print("====================== checkpoint 3 =======================")
        
        # Add rightmost char
        right = txt[i]
        window_count[right] += 1
        if window_count[right] == pat_count[right]:
            matches += 1                    # New perfect match!
        
        # Remove leftmost char  
        left = txt[i - len(pat)]
        window_count[left] -= 1
        if window_count[left] < pat_count[left]:
            matches -= 1                    # Lost a perfect match
        
        print("====================== checkpoint 4 =======================")
        print("pat_count = "+str(pat_count))
        print("required = "+str(required))
        print("window_count = "+str(window_count))
        print("matches = "+str(matches))
        print("====================== checkpoint 4 =======================")

        if matches == required: return True # Found permutation!
    
    return False 
    
if __name__ == "__main__":
    txt = "geeks"
    pat = "eke"
    if check_permutation_substring(txt, pat):
        print("true")
    else:
        print("false")
