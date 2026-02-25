"""

Maximum Sum of a Subarray with K Elements

"""

import sys

"""
def maxSum_without_sliding_window(arr, n, k):
    # Initialize result
    max_sum = -sys.maxsize
    #print(max_sum)
    # Consider all blocks starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]

        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum

if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    n = len(arr)
    print(maxSum_without_sliding_window(arr, n, k))
"""

def maxSum(arr, k):
    
    # length of the array
    n = len(arr)

    # n must be greater than k
    if n <= k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum

    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum

if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(maxSum(arr, k))

