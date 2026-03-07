"""
Given a list of n integers, write a function that rotates
the array to the right by 1 position.
"""

def rotate_array(arr):
    prev_temp = arr[-1]
    for ind in range(len(arr)):
        curr_temp = arr[ind]
        arr[ind] = prev_temp
        prev_temp = curr_temp

    return arr

if __name__ == "__main__":
    inp = [1, 2, 3, 4, 5]
    print(rotate_array(inp))
