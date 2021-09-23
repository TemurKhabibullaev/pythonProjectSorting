import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
import random

# Best O(n`2) / Worst O(n`2)
def selectionSort(array):
    first = 0
    last = len(array)
    while first < len(array) - 1:
        for i in range(first+1, last):
            if array[first+1] < array[first]:
                array[first], array[first+1] = array[first+1], array[first]
                first += 1
            else:
                last += 1
    return array


# Best O(n) / Worst O(n`2)
def insertionSort(array):
    for i in range(1, len(array)):
        a = i
        while a > 0 and array[a] < array[a - 1]:
            array[a-1], array[a] = array[a], array[a-1]
            a -= 1
    return array


# Best O(n) / Worst O(n`2)
def bubbleSort(array):
    locker = 0
    swap = False
    while swap is False:
        swap = True
        for i in range(len(array)-1-locker):
            if array[i] > array[i + 1]:
                array[i+1], array[i] = array[i], array[i+1]
                swap = False
        locker += 1
    return array


# Best O(nlog(n)) / Worst O(nlog(n))

def heapSort(array):
    return array

def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]


def quicksort(A, lef, rig):
    if lef >= rig:
        return

    pivot = A[rig]
    pivotIdx = lef

    for i in range(lef, rig):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, rig, pivotIdx)
    yield A

    yield from quicksort(A, lef, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, rig)


def radixSort(array):
    return array

