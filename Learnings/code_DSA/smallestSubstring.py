"""
Given a string S of size N consisting of the characters 0, 1 and 2, the task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Examples:

Input: S = "01212"
Output: 3
Explanation: The substring 012 is the smallest substring that contains the characters 0, 1 and 2.

Input:  S = "12121"
Output: -1
Explanation:  As the character 0 is not present in the string S, therefore no substring containing all the three characters 0, 1 and 2 exists. Hence, the answer is -1 in this case.

"""

"""

const smallestSubstring = (S) => {
            let res = 9999999;

            // To check 0, 1 and 2
            let zero = false, one = false, two = false;

            // To store indexes of 0, 1 and 2
            let zeroindex, oneindex, twoindex;
            for (let i = 0; i < S.length; i++) {
                if (S[i] == "0") {
                    zero = true;
                    zeroindex = i;
                }
                else if (S[i] == "1") {
                    one = true;
                    oneindex = i;
                }
                else if (S[i] == "2") {
                    two = true;
                    twoindex = i;
                }

                // Calculating length
                if (zero && one && two)
                    res = Math.min(res,
                        Math.max(...[zeroindex, oneindex, twoindex])
                      - Math.min(...[zeroindex, oneindex, twoindex]));
            }

            // In case if there is no substring that contains 0,1 and 2
            if (res == 9999999)
                return -1;
            return res + 1;
        }

        // Driver Code
        let S = "01212";

// Function call
console.log(smallestSubstring(S));



def smallestSubstring(S):

    # Initialize variables
    n, i, j, k, cnt, min_len = len(S), 0, 0, 0, 0, float("inf")

    # Frequency array
    freq = [0] * 3
    #print(freq)
    while k < n:
        freq[int(S[k])] += 1
        if freq[int(S[k])] == 1:
            cnt += 1
        print("====================== checkpoint 1 =======================")
        print("S[k] = "+S[k])
        print("freq = "+str(freq))
        print("min_len = "+str(min_len))
        print("cnt = "+str(cnt))
        print("i = "+str(i))
        print("S[i] = "+str(S[i]))
        if cnt == 3:
            while freq[int(S[i])] > 1:
                freq[int(S[i])] -= 1
                i += 1
                print("====================== checkpoint 2 =======================")
                print("S[k] = "+S[k])
                print("freq = "+str(freq))
                print("min_len = "+str(min_len))
                print("cnt = "+str(cnt))
                print("i = "+str(i))
                print("S[i] = "+str(S[i]))
            min_len = min(min_len, k - i + 1)
            freq[int(S[i])] -= 1
            i += 1
            cnt -= 1
            print("====================== checkpoint 3 =======================")
            print("S[k] = "+S[k])
            print("freq = "+str(freq))
            print("min_len = "+str(min_len))
            print("cnt = "+str(cnt))
            print("i = "+str(i))
            print("S[i] = "+str(S[i]))
        k += 1
    #print(freq)
    return -1 if min_len == float("inf") else min_len

"""

def smallestSubstring(s: str) -> int:
    n = len(s)
    count = {'0': 0, '1': 0, '2': 0}  # frequency in current window
    have = 0                         # how many of '0','1','2' are present
    need = 3
    left = 0
    ans = float('inf')

    for right, ch in enumerate(s):
        print("====================== checkpoint 1 =======================")
        print("right = "+str(right))
        print("left = "+str(left))
        print("ans = "+str(ans))
        print("s = "+str(s))
        print("count = "+str(count))
        print("====================== checkpoint 1 =======================")
        if ch in count:
            if count[ch] == 0:
                have += 1
            count[ch] += 1
        
        # Try to shrink from the left while window has all 3 chars
        while have == need:
            print("====================== checkpoint 2 =======================")
            print("right = "+str(right))
            print("left = "+str(left))
            print("ans = "+str(ans))
            print("s = "+str(s))
            print("count = "+str(count))
            print("====================== checkpoint 2 =======================")
            ans = min(ans, right - left + 1)
            left_ch = s[left]
            if left_ch in count:
                count[left_ch] -= 1
                if count[left_ch] == 0:
                    have -= 1
            left += 1

    return ans if ans != float('inf') else -1


# Driver code
S = "3011212"

print(smallestSubstring(S))