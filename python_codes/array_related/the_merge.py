"""
Given two separately sorted arrays, merge them into one sorted array.
Example:
Input:  [1, 3, 5, 7]  and  [2, 4, 6, 8]
Output: [1, 2, 3, 4, 5, 6, 7, 8]

Input:  [1, 5, 9]  and  [2, 3, 4, 6]
Output: [1, 2, 3, 4, 5, 6, 9]

Constraints:

Do NOT use Python's built-in sort
Think about using two pointers — one for each array
State the time complexity
"""
from typing import List
def merge_sort(arr_A:List, arr_B:List) -> List:
    i, j = 0, 0
    merged = []

    # walk while both arrays still have elements
    while i < len(arr_A) and j < len(arr_B):
        if arr_A[i] <= arr_B[j]:
            merged.append(arr_A[i])
            i += 1
        else:
            merged.append(arr_B[j])
            j += 1

    # one of the arrays may have leftovers
    while i < len(arr_A):
        merged.append(arr_A[i])
        i += 1

    while j < len(arr_B):
        merged.append(arr_B[j])
        j += 1

    return merged



if __name__ == "__main__":
    test1, test2 = [1, 5, 9], [2, 3, 4, 6]
    print(merge_sort(test2, test1))