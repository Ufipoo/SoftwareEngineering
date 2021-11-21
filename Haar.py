import numpy as np
from datetime import datetime


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = np.size(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


for j in range(10, 10000, 100):
    list_time = []
    for i in range(10):
        arr = np.random.randint(0, 100, 1000)
        #print(arr)
        startTime = datetime.now()
        quick_sort(arr)
        #print("Time taken:", datetime.now() - startTime)
        #print("Sorted array is:")
        #print(arr)
        time_al = datetime.now() - startTime
        list_time.append("0.{}".format(time_al.microseconds))
        #print("Time taken:", time_al)
        with open('output_Quick.txt', 'a') \
                as outFile: outFile.write(str(i) + ' ' + str(j) + ' ' + str(time_al.microseconds)
                                          + '\n')
    with open('output_Quick.txt', 'a') \
        as outFile: outFile.write('---------------' + '\n')
    with open('QuickSort_best_time_epoch.txt', 'a') \
            as outFile:
        outFile.write(str(min(list_time)) + '\n')
