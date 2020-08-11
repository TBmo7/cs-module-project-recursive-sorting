# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #elements = len(arrA) + len(arrB)#elements is the length of the incoming array(s)?
    #merged_arr = [0] * elements
    merged_arr = []
    
    # Your code here
    """A_end = elements // 2
    B_start = A_end +1
    size = A_end - B_start + 1

    index = arrA
    if len(merged_arr) > 0:

        while len(arrA) <= A_end and B_start <= len(arrB):
            if arrA[]   """ 
    """
    left, right = 0, 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    merged_arr += arrA[left:]
    merged_arr == arrB[right:]
    """
    """
    if len(merged_arr) > 0:
        indexA, indexB = 0, 0
        index = 0
    
        while indexA < len(arrA) and indexB < len(arrB):
    
            #index = (elements // 2) -1
            #while index < elements:
            
                if arrA[index] < arrB[index]:
                    #merged_arr.append(arrA[index])
                    merged_arr[index] = arrA[indexA]
                    indexA +=1
            
            
                else:
                    #merged_arr.append(arrB[index])
                    merged_arr[index] = arrB[indexB]
                    indexB +=1
            #index += 1            
    """
    """
    if arrA and arrB:
        if arrA[0] > arrB[0]:
            arrA , arrB = arrB , arrA
        return [arrA[0] + merge(arrA[1:], arrB)]
    merged_arr = arrA + arrB
    """

    if not arrA and not arrB:
        return []
    if not arrA:
        return [arrB[0]] + merge(arrA,arrB[1:])
    if not arrB:
        return [arrA[0]] + merge(arrA[1:], arrB)
    if arrA[0] > arrB[0]:
        return [arrB[0]] + merge(arrA, arrB[1:])
    merged_arr = [arrA[0]] + merge(arrA[1:], arrB)




    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
#similar to binary sort here

def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) #using slice notation here, this gets beginning through middle -1
    right = merge_sort(arr[mid:]) # gets middle -1 to the rest of the array

    return merge(left,right)
    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass            

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
