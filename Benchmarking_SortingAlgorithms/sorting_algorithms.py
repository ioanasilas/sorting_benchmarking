import random
import sys
sys.setrecursionlimit(10**9)

"""
Sorting algorithms and their implementation that can be benchmarked
"""

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 0
        if flag == 1:
            break

# Insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge sort
def merge1(arr, arr1, arr2):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge1(arr, left, right)

# Quick sort (random pivot)
def partition(arr, start, end):
    pIndex = random.randint(start, end)
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex

def quick_sort(arr, start, end):
    if start < end:
        partitionIndex = partition(arr, start, end)
        quick_sort(arr, start, partitionIndex - 1)
        quick_sort(arr, partitionIndex + 1, end)

# Timsort
def binary_search(arr, value, lIndex, rIndex):
  while (lIndex <= rIndex):
    mid = (lIndex + rIndex) // 2
    if value < arr[mid]:
      rIndex = mid - 1
    else:
      lIndex = mid + 1
  return lIndex

def binary_insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        pos = binary_search(arr, key, start, i - 1)
        j = i
        while j > pos:
           arr[j] = arr[j - 1]
           j -= 1
        arr[pos] = key

def merge2(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    i, j, k = 0, 0, left
    while i < len(left_copy) and j < len(right_copy):
       if left_copy[i] < right_copy[j]:
          arr[k] = left_copy[i]
          i += 1
       else:
          arr[k] = right_copy[j]
          j += 1
       k += 1
       # if any remainding elements are left
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

def compute_minrun(n):
    """Function that computes an efficient minrun size to ensure balanced merges."""
    shift = max(0, n.bit_length() - 6)
    minrun = max(1, n >> shift)
    # to check if there are any remaining bits set after the shift
    if n & ((1 << shift) - 1):
        minrun += 1
    return minrun

def timsort(arr):
  n = len(arr)
  min_run = compute_minrun(n)
  # for each run we apply insertion sort
  for index in range(0, n, min_run):
     end = min(n - 1, index + min_run - 1)
     binary_insertion_sort(arr, index, end)
  # merging of the sorted runs
  size = min_run
  while size < n:
    for left in range(0, n, 2 * size):
        mid = min(n - 1, left + size - 1)
        right = min(n - 1, left + 2 * size - 1)
        if mid < right:
           merge2(arr, left, mid, right)
    size *= 2  
   
# Heapsort
def fix_down(arr, k, n):
  j = 0
  # loop that makes sure that element at index k is moved down to maintain heap property
  while 2 * k <= n:
    j = 2 * k # child of k
    # select larger child
    if j < n and arr[j] < arr[j + 1]:
      j += 1
    # if parent is not less than largest child, stop loop
    if not arr[k] < arr[j]:
      break
    arr[k], arr[j] = arr[j], arr[k]
    k = j

def heap_sort(arr, l, r):
  n = r - l + 1
  # adjust for 1 based indexing
  heap = [None] + arr[l:r+1]
  n = len(heap) - 1
  for k in range (n // 2, 0, -1):
    fix_down(heap, k, n)

  # sorting the heap
  while n > 1:
    heap[1], heap[n] = heap[n], heap[1]
    n -= 1
    fix_down(heap, 1, n)
  # copy the sorted elements back to the original list
  arr[l:r+1] = heap[1:]