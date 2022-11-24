from random import randint
import time
from functools import wraps
import sys

sys.setrecursionlimit(100000000)


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def produce_random_dataset(dataset_size):

    dataset = []

    for i in range(dataset_size):

        dataset.append(randint(0, dataset_size))

    return dataset


# Heap Sort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # See if right child of root exists and is
 # greater than root
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # Change root, if needed
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
  # Heapify the root.
 
        heapify(arr, n, largest)
 
 
# The main function to sort an array of given size
 
@timeit
def heapSort(arr):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
#-----------------------------------

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 


@timeit
def do_merge_sort(dataset):
    
    mergeSort(dataset, 0, len(dataset)-1)
    


 
#-----------------------------------

#quicksort
    

def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
    
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

        
@timeit
def do_quick_sort(dataset):
    quickSort(dataset, 0, len(dataset) - 1)
    return dataset

#-----------------------------------

#Eray sort --------------- 
def compare(dataset):

    data_length = len(dataset)

    if data_length <= 1:

        if data_length == 0:

            return
        
        return dataset
    
    last_index = 1
    compare_index = 0

    while last_index < data_length:
        
        if dataset[last_index] > dataset[compare_index]:
            
            compare_index = last_index
            
        else:

            if dataset[last_index] < dataset[compare_index]:
                
                pass
                
            else:
                      
                compare_index = last_index
                
        last_index += 1
    
    return compare_index

def find_best(best, dataset, new_dataset):
    if best == 0:
        return new_dataset
    else :
        new_dataset.append(dataset.pop(compare(dataset)))
        best -= 1
        find_best(best, dataset, new_dataset)

@timeit
def eray_sort(dataset):
    new_dataset = []
    find_best(len(dataset)-1, dataset, new_dataset)
    return new_dataset
#-----------------------------------


def main():
    dataset_lenght = 2000
    
    
    print("--------------------")

    for i in range(100, dataset_lenght + 100, 100):
        dataset = produce_random_dataset(i)
        print(f"Dataset size: {i}")
        do_quick_sort(dataset)
        do_merge_sort(dataset)
        heapSort(dataset)
        eray_sort(dataset)
        print("--------------------")

    

if __name__ == '__main__':
    main()


        