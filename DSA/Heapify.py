arr = [10,7,6,4,5,4,5,3,2]

def heapify(arr,ind,val):
    if arr[ind] > val:
        arr[ind] = val
        heapifyDown(arr,ind)

    else:
        arr[ind] = val
        heapifyUp(arr,ind)
    return arr

def heapifyDown(arr,ind):
    n = len(arr)
    largest_ind = ind

    leftChild_ind = 2 * ind + 1
    rightChild_ind = 2 * ind + 2

    #If left child holds the larger value, update the largest index
    if(leftChild_ind < n and arr[leftChild_ind] > arr[largest_ind]):
        largest_ind = leftChild_ind
        
    #If right child holds the larger value, update the largest index
    if(rightChild_ind < n and arr[rightChild_ind] > arr[largest_ind]):
        largest_ind = rightChild_ind

    #If the largest is not the current Index, swap and heapify down
    if largest_ind != ind:
        arr[largest_ind], arr[ind] = arr[ind], arr[largest_ind]
        heapifyDown(arr,largest_ind)

def heapifyUp(arr,ind):
    parent_ind = (ind-1) // 2

    if(ind > 0 and arr[ind] > arr[parent_ind]):
        arr[ind], arr[parent_ind] = arr[parent_ind], arr[ind]
        heapifyUp(arr, parent_ind)


print(heapify(arr,0,1))