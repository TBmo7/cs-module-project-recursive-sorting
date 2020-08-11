arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]


# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #if array is not none
    #find a mid point (start + end) // 2
    #if mid point == target return target
    #if mid > target: 
    #   binary_search(arr, target, start, mid)
    #else:
    #   binary_search(arr,target,mid,end)
    if len(arr) > 0:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        else:
            if arr[middle] > target:
                return binary_search(arr,target,start,middle)
            else:
                return binary_search(arr,target,middle,end)
    else:
        return -1 





# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

print(binary_search(arr1, -8, 0, len(arr1)-1))


