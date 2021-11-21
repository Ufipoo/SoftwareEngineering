import matplotlib.pyplot as plt
import datetime
def open_file(file):
    list_time = []
    spisok = file.readlines()
    for line in spisok:
        #list_time.append(line)
        parts = line.split()
        for i in range(0, len(parts)):
            list_time.append(float(parts[i]))
    return list_time

ll = open_file(open('InsertionSort_best_time_epoch.txt'))
kk = open_file(open('QuickSort_best_time_epoch.txt'))
print(ll)
print(kk)
x = []
for i in range(10, 10000, 100):
    x.append(i)
print(x)
plt.plot(x, ll, label=u'Сортировка вставками', color='red')
plt.plot(x, kk, label=u'Быстрая сортировка', color='blue')

plt.grid(True)
plt.title('График сравнения алгоритмов сортировки')
plt.xlabel('Объем массива')
plt.ylabel('Затраченное время')
plt.legend(loc='best')
plt.show()