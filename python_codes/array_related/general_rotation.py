"""
Given a list of n integers, write a function that rotates
the array to the right or left by k position.
"""
from typing import List


def reverse(arr: List, left: int, right: int) -> None:
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def left_rotation(arr: List, k: int):
    n = len(arr)
    k = k % n          # handles k >= n and k = 0
    if k == 0:
        return
    reverse(arr, 0, n-1)
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-k-1)

def right_rotation(arr: List, k: int):
    n = len(arr)
    k = k % n          # handles k >= n and k = 0
    if k == 0:
        return
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [1, 2, 3, 4, 5, 6, 7]
    left_rotation(a, 2)
    right_rotation(b, 2)
    print(f"after left rotation the list a will be: {a}\n"
          f"after right rotation the list b will be : {b}")
