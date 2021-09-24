import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
import random


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


# Insertion algo
def insertionsort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            if j != j-1:
                array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            yield array


# Merge algo
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


# Merge algo helper
def mergesort(array, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(array, start, mid)
    yield from mergesort(array, mid + 1, end)
    yield from merge(array, start, mid, end)
    yield array


# Quick algo
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


# Bubble algo
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
num = int(input("Enter the number of random integers and the max number in the list: "))

# random integers in a list.
arrayRan = [x + 1 for x in range(num)]
random.seed(time.time())
random.shuffle(arrayRan)
if algoType == 1:
    topBar = "Quick Sort on Average: O(nlog(n))"
    generator = quicksort(arrayRan, 0, num - 1)
elif algoType == 2:
    topBar = "Merge Sort on Average: O(nlog(n))"
    generator = mergesort(arrayRan, 0, num - 1)
elif algoType == 3:
    topBar = "Selection Sort on Average: O(n`2)"
    generator = selectionsort(arrayRan)
elif algoType == 4:
    topBar = "Insertion Sort on Average: O(n`2)"
    generator = insertionsort(arrayRan)
else:
    topBar = "Bubble Sort on Average: O(n`2)"
    generator = bubblesort(arrayRan)

# Create the full figure + axis
fig, ax = plt.subplots()
ax.set_title(topBar)
# bar plot
barRectangles = ax.bar(range(len(arrayRan)), arrayRan, align="edge")
# initializing x and y limits
ax.set_xlim(0, num)
ax.set_ylim(0, int(1.07 * num))
# Label
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
# This function is basically a frame refresher
iteration = [0]


# Frame updater
def updateFrames(array, rects, iteration):

    for rect, val in zip(rects, array):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text(f"It took {iteration[0]} operations to complete")


t0 = time.time()
performer = animation.FuncAnimation(fig, func=updateFrames, fargs=(barRectangles, iteration), frames=generator, interval=1,
                                    repeat=False)

plt.show()
t1 = time.time()
print(round(t1-t0))
