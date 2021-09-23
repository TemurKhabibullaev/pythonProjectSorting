import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
from random import randrange
import random
import numpy as np

# Sorting Algos:
def selectionsort(array):
    if len(array) == 1:
        return

    for i in range(len(array)):
        minVal = array[i]
        minIdx = i
        for j in range(i, len(array)):
            if array[j] < minVal:
                minVal = array[j]
                minIdx = j
            yield array
        if i != minIdx:
            array[i], array[minIdx] = array[minIdx], array[i]
        yield array


def insertionsort(array):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            if j != j-1:
                array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            yield array


def merge(array, start, mid, end):

    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if array[leftIdx] < array[rightIdx]:
            merged.append(array[leftIdx])
            leftIdx += 1
        else:
            merged.append(array[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(array[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(array[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array


def mergesort(array, start, end):

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(array, start, mid)
    yield from mergesort(array, mid + 1, end)
    yield from merge(array, start, mid, end)
    yield array


def quicksort(array, start, end):

    if start >= end:
        return

    pivot = array[end]
    pivotIdx = start

    for i in range(start, end):
        if array[i] < pivot:
            if i != pivotIdx:
                array[i], array[pivotIdx] = array[pivotIdx], array[i]
            pivotIdx += 1
        yield array
    if end != pivotIdx:
        array[end], array[pivotIdx] = array[pivotIdx], array[end]
    yield array

    yield from quicksort(array, start, pivotIdx - 1)
    yield from quicksort(array, pivotIdx + 1, end)


def bubblesort(array):

    if len(array) == 1:
        return

    swapped = True
    for i in range(len(array) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                if j != j + 1:
                    array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
            yield array


# User's input:
algoType = int(input("Which sorting method you want?\n1.Quick\n2.Merge\n3.Selection\n4.Insertion\n5.Bubble\n"))
num = int(input("Enter the number of random integers in the list: "))

# Build and randomly shuffle list of integers.
array = [x + 1 for x in range(num)]
random.seed(time.time())
random.shuffle(array)
if algoType == 1:
    topBar = "Quick Sort on Average: O(nlog(n))"
    generator = quicksort(array, 0, num - 1)
elif algoType == 2:
    topBar = "Merge Sort on Average: O(nlog(n))"
    generator = mergesort(array, 0, num - 1)
elif algoType == 3:
    topBar = "Selection Sort on Average: O(n`2)"
    generator = selectionsort(array)
elif algoType == 4:
    topBar = "Insertion Sort on Average: O(n`2)"
    generator = insertionsort(array)
else:
    topBar = "Bubble Sort on Average: O(n`2)"
    generator = bubblesort(array)

# Initialize figure and axis.
fig, ax = plt.subplots()
ax.set_title(topBar)

# Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
# list of rectangles (with each bar in the bar plot corresponding
# to one rectangle), which we store in bar_rects.
bar_rects = ax.bar(range(len(array)), array, align="edge")

# Set axis limits. Set y axis upper limit high enough that the tops of
# the bars won't overlap with the text label.
ax.set_xlim(0, num)
ax.set_ylim(0, int(1.07 * num))

# Place a text label in the upper-left corner of the plot to display
# number of operations performed by the sorting algorithm (each "yield"
# is treated as 1 operation).
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

# Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
# To track the number of operations, i.e., iterations through which the
# animation has gone, define a variable "iteration". This variable will
# be passed to update_fig() to update the text label, and will also be
# incremented in update_fig(). For this increment to be reflected outside
# the function, we make "iteration" a list of 1 element, since lists (and
# other mutable objects) are passed by reference (but an integer would be
# passed by value).
# NOTE: Alternatively, iteration could be re-declared within update_fig()
# with the "global" keyword (or "nonlocal" keyword).
iteration = [0]


def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("It took {} operations to complete".format(iteration[0]))


anim = animation.FuncAnimation(fig, func=update_fig,
                               fargs=(bar_rects, iteration), frames=generator, interval=1,
                               repeat=False)
plt.show()

