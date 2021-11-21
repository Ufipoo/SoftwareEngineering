import numpy as np
from datetime import datetime


def insertion_sort(arr):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, np.size(arr)):
        key = arr[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i-1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


for j in range(10, 10000, 100):
    list_time = []
    for i in range(10):
        arr = np.random.randint(0, 100, 1000)
        #print(arr)
        startTime = datetime.now()
        insertion_sort(arr)
        #print("Time taken:", datetime.now() - startTime)
        #print("Sorted array is:")
        #print(arr)
        time_al = datetime.now() - startTime
        list_time.append("0.{}".format(time_al.microseconds))
        #print("Time taken:", time_al)
        with open('output.txt', 'a') \
                as outFile: outFile.write(str(i) + ' ' + str(j) + ' ' + str(time_al.microseconds)
                                          + '\n')
    with open('output.txt', 'a') \
        as outFile: outFile.write('---------------' + '\n')
    with open('InsertionSort_best_time_epoch.txt', 'a') \
            as outFile:
        outFile.write(str(min(list_time)) + '\n')