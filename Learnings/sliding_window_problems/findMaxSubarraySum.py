"""

Maximum sum subarray having sum less than or equal to given sum

You are given an array of non-negative integers and a target sum. Your task is to find a contiguous subarray whose sum is the maximum possible, while ensuring that it does not exceed the given target sum.

Note: The given array contains only non-negative integers.

Examples: 

Input: arr[] = [1, 2, 3, 4, 5], sum = 11
Output: 10
Explanation: Subarray having maximum sum is [1, 2, 3, 4]


Input: arr[] = [2, 4, 6, 8, 10], sum = 7
Output: 6
Explanation: Subarray having maximum sum is [2, 4]or [6]

"""

from typing import List

def max_subarray_sum_at_most_k(arr: List[int], k: int) -> int:
    n = len(arr)
    max_sum = 0
    current_sum = 0
    start = 0

    for end in range(n):
        # Expand window to the right
        current_sum += arr[end]

        # Shrink window from the left while sum > k
        while start <= end and current_sum > k:
            current_sum -= arr[start]
            start += 1

        # Now current_sum <= k; update answer
        if current_sum <= k:
            max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5] 
    sum = 11

    print(max_subarray_sum_at_most_k(arr, sum))