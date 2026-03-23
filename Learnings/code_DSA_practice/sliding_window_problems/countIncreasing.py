"""

Count Strictly Increasing Subarrays

Given an integer array arr[], the task is to count the number of subarrays in arr[] that are strictly increasing and have a size of at least 2. A subarray is a contiguous sequence of elements from arr[]. A subarray is strictly increasing if each element is greater than its previous element.

Examples:

Input: arr[] = [1, 4, 5, 3, 7, 9]
Output: 6
Explanation: The strictly increasing subarrays are: [1, 4], [1, 4, 5], [4, 5], [3, 7], [3, 7, 9], [7, 9]

Input: arr[] = [1, 3, 3, 2, 3, 5]
Output: 4
Explanation: The strictly increasing subarrays are: [1, 3], [2, 3], [2, 3, 5], [3, 5] 

Input: arr[] = [2, 2, 2, 2]
Output: 0
Explanation: No strictly increasing subarray exists.

"""

# Python Code to count strictly increasing 
# subarrays using Length based Formula

# Function to count strictly increasing 
# subarrays

from typing import List

def count_strictly_increasing_subarrays(arr: List[int]) -> int:
    n = len(arr)
    if n < 2:
        return 0

    total = 0
    length = 1  # length of current strictly increasing run

    for i in range(1, n):
        if arr[i] > arr[i - 1]:

            print("====================== checkpoint 1 =======================")
            print("arr = "+str(arr))
            print("length = "+str(length))
            print("total = "+str(total))
            print("====================== checkpoint 1 =======================")    

            length += 1
        else:

            print("====================== checkpoint 2 =======================")
            print("arr = "+str(arr))
            print("length = "+str(length))
            print("total = "+str(total))
            print("====================== checkpoint 2 =======================")    

            # end of current increasing run
            if length >= 2:
                total += (length * (length - 1)) // 2 #operator performs floor division
            length = 1  # restart from current element

    print("====================== checkpoint 3 =======================")
    print("arr = "+str(arr))
    print("length = "+str(length))
    print("total = "+str(total))
    print("====================== checkpoint 3 =======================")    

    # add contribution of the last run
    if length >= 2:
        total += (length * (length - 1)) // 2 #operator performs floor division

    return total 


# Driver code
if __name__ == "__main__":
    
    arr = [1, 4, 5, 3, 7, 9]
    
    print(count_strictly_increasing_subarrays(arr))