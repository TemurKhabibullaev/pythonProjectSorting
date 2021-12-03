import matplotlib.pyplot as plt
import time, random
import numpy as np
from matplotlib.animation import FuncAnimation


# Selection Sort
def selectionsort(array):
    if len(array) == 1:
        return
    for index in range(len(array)):
        minValue = array[index]
        minIdex = index
        for j in range(index, len(array)):
            if array[j] < minValue:
                minValue = array[j]
                minIdex = j
            yield array
        if index != minIdex:
            array[index], array[minIdex] = array[minIdex], array[index]
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
    leftIndex = start
    rightIndex = mid + 1
    while leftIndex <= mid and rightIndex <= end:
        if array[leftIndex] < array[rightIndex]:
            merged.append(array[leftIndex])
            leftIndex += 1
        else:
            merged.append(array[rightIndex])
            rightIndex += 1
    while leftIndex <= mid:
        merged.append(array[leftIndex])
        leftIndex += 1
    while rightIndex <= end:
        merged.append(array[rightIndex])
        rightIndex += 1
    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array


# Merge algo helper
def mergesort(array, start, end):
    if end <= start:
        return
    midPoint = start + ((end - start + 1) // 2) - 1
    yield from mergesort(array, start, midPoint)
    yield from mergesort(array, midPoint + 1, end)
    yield from merge(array, start, midPoint, end)
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
    swap = True
    for i in range(len(array) - 1):
        if not swap:
            break
        swap = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                if j != j + 1:
                    array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
            yield array


# User's input:
sortingAlgorithmsChoice = int(input("Which sorting method you want?\n1.Quick\n2.Merge\n3.Selection\n4.Insertion\n5.Bubble\n"))
numberOfRandomIntegers = int(input("Enter the number of random integers and the max number in the list: "))
# random integers in a list.
arrayOfRandom = [x + 1 for x in range(numberOfRandomIntegers)]
random.seed(time.time())
random.shuffle(arrayOfRandom)
if sortingAlgorithmsChoice == 1:
    topBar = "Quick Sort on Average: O(nlog(n))"
    generator = quicksort(arrayOfRandom, 0, numberOfRandomIntegers - 1)
elif sortingAlgorithmsChoice == 2:
    topBar = "Merge Sort on Average: O(nlog(n))"
    generator = mergesort(arrayOfRandom, 0, numberOfRandomIntegers - 1)
elif sortingAlgorithmsChoice == 3:
    topBar = "Selection Sort on Average: O(n^2)"
    generator = selectionsort(arrayOfRandom)
elif sortingAlgorithmsChoice == 4:
    topBar = "Insertion Sort on Average: O(n^2)"
    generator = insertionsort(arrayOfRandom)
else:
    topBar = "Bubble Sort on Average: O(n^2)"
    generator = bubblesort(arrayOfRandom)

colors = ['black', 'red', 'green', 'yellow', 'cyan']


def plot3D(numbers, array, generator, topBar):
    plt.style.use('fivethirtyeight')

    # Create the full figure + axis
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    z, dx, dy, dz = np.zeros(numbers), np.ones(numbers), np.ones(numbers), [i for i in range(len(array))]

    # 3D bars:
    rects = ax.bar3d(range(len(array)), array, z, dx, dy, dz, color="grey")
    # initializing x and y limits
    ax.set_xlim(0, len(array))
    ax.set_ylim(0, int(1.1 * len(array)))
    ax.set_title(topBar, fontdict={'fontsize': 13, 'fontweight': 'medium', 'color': 'black'})

    # 2D text placed on the upper left based on the axes fraction
    text = ax.text2D(0.1, 0.95, "", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color="grey")
    iteration, startTime = [0], time.time()
    # frame refresher & updater
    randomColor = np.random.choice(colors)

    def frames(A, rects, iteration, t0):
        ax.collections.clear()

        ax.bar3d(range(len(array)), A, z, dx, dy, dz, color=randomColor, shade=True)
        iteration[0] += 1
        text.set_text(f"{iteration[0]} Operations | {round(time.time()-t0)} Seconds")

    animate = FuncAnimation(fig, func=frames, fargs=(rects, iteration, startTime), frames=generator, interval=50, repeat=False)
    plt.show()


plot3D(numberOfRandomIntegers, arrayOfRandom, generator, topBar)
