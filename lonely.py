"""
    Given an array of integers, where all elements but one occur twice, find the unique element.

Example

a = [ 1,2,3,4,3,2,1]

The unique element is 4.

"""

def lonely(arr):
    for i in range(len(arr)-1):
        if arr.count(arr[i]) == 1:
            print(f"o número único é {arr[i]}")

arr = [ 1,2,3,4,3,2,1]
lonely (arr)