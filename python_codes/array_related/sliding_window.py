"""
Given a list of integers and a window size k, return a list
of the maximum value in each window as it slides from
left to right.

Example:
Input:  [1, 3, -1, -3, 5, 3, 6, 7],  k = 3
Output: [3, 3, 5, 5, 6, 7]

Explanation:
Window [1,3,-1]  → max = 3
Window [3,-1,-3] → max = 3
Window [-1,-3,5] → max = 5
Window [-3,5,3]  → max = 5
Window [5,3,6]   → max = 6
Window [3,6,7]   → max = 7

"""
from typing import List
def sliding_window(array:List, k:int)-> List:
    sliding_array = list()
    n = len(array)

    for ind in range(n):
        max_value = array[ind]
        if ind + k <= n:
            for j in range(ind, ind+k):
                if array[j] > max_value:
                    max_value = array[j]
                else:
                    pass
            sliding_array.append(max_value)


    return sliding_array

if __name__ == "__main__":
    test = [5, 1, 2, 3]
    K = 2
    print(sliding_window(test, K))