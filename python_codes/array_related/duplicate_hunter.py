"""
Given a list of n integers, return True if any value
appears more than once. Return False if all elements are unique.

"""
from typing import List

def naive_solution(arr:List) -> bool :
    for i in range(len(arr)):
        comp = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def solution_using_set(arr):
    seen= set()
    for ele in arr:
        if ele in seen:
            return True
        else:
            seen.add(ele)
    return False



if __name__ == '__main__':
    example_1 = [4, 2, 7, 2, 9]
    example_2 = [1, 3, 5, 7]
    print(naive_solution(example_1))
    print(naive_solution(example_2))
    print(solution_using_set(example_1))
    print(solution_using_set(example_2))