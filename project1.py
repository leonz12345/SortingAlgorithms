"""
Math 560
Project 1
Fall 2021

Partner 1: Leon Zhang
Partner 2: Powen Hsiao
Date: 21th Oct 2021
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    for i in range(len(listToSort)):
        # Find the smallest value's index from the unsorted part of array
        smallest_idx = i
        for j in range(i+1,len(listToSort)): # i-1 elements sorted
            if listToSort[j] < listToSort[smallest_idx]: # Check value is smaller than current smallest
                smallest_idx = j # Update index of smallest
        # Make swap
        listToSort[i], listToSort[smallest_idx] = listToSort[smallest_idx], listToSort[i]
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for i in range(1,len(listToSort)):
        current = listToSort[i] # Save the ith element
        j = i-1
        # Find the place to insert from the sorted part
        while j >= 0 and current < listToSort[j] :
            listToSort[j + 1] = listToSort[j] # Move bigger element than current one place ahead
            j -= 1
        # Insert the ith value to the sorted part of the array
        listToSort[j + 1] = current
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    if len(listToSort) < 2:
        return listToSort
    swapped = True
    k = 0
    while swapped:
        swapped = False
        for i in range(len(listToSort) - 1 - k):
            if listToSort[i] > listToSort[i + 1]:
                temp = listToSort[i]
                listToSort[i] = listToSort[i + 1]
                listToSort[i + 1] = temp
                swapped = True
        k += 1
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    if len(listToSort) > 1:
        # Split the array to left and right half
        mid = len(listToSort)//2 # Middle index
        left = MergeSort(listToSort[:mid]) # Recursive call of the left half
        right = MergeSort(listToSort[mid:]) # Recursive call of the right half
        # Merge two sorted array
        i = j = k = 0 # i: index of left, j: index of right, k: index of listToSort
        # Sort min(len(left), len(right)) first
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                listToSort[k] = left[i]
                i += 1
            else:
                listToSort[k] = right[j]
                j += 1
            k += 1
        # If left side has more, then add the left to sorted
        while i < len(left):
            listToSort[k] = left[i]
            i += 1
            k += 1
        # If right side has more, then add the right to sorted
        while j < len(right):
            listToSort[k] = right[j]
            j += 1
            k += 1
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None. 
    if j == None:
        j = len(listToSort)
    if len(listToSort) <= 1:
        return listToSort
    p = (i + j - 1)//2
    small = []
    large = []
    for ptr in range(i , j):
        if ptr != p:
            if listToSort[ptr] <= listToSort[p]:
                small.append(listToSort[ptr])
            else:
                large.append(listToSort[ptr])
    return QuickSort(small, 0, len(small)) + [listToSort[p]] + QuickSort(large, 0, len(large))
#    listToSort = small + [listToSort[p]] + large
#    QuickSort(listToSort, i, p + 1)
#    QuickSort(listToSort, p + 1, j)


"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    
#    print('DEFAULT measureTime')
 #   print()
  #  measureTime()
