import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve
#==================================================
sus= open("result.txt", "w")
data = []
for i in open("input_101.txt"):
    data.append(int(i.strip()))
data = np.delete(data, 0)

lens = len(data)
data = sorted(data)

print("Послідовність:", data)
sus.write("Послідовність:" + str(data))


#==================================================
def task1(num):
    index = num * (lens + 1) - 1
    result = data[int(index)] + (index % int(index)) * (data[int(index) + 1] - data[int(index)])
    return result
#==================================================
def task2():
    sum = 0
    totalsum = 0
    totalSum = 0
    for i in range(lens):
        sum += data[i]

    for i in range(lens):
        totalsum += (data[i] - (sum / lens)) ** 2
        totalSum += abs(data[i] - (sum / lens))

    result = totalsum / lens
    Result = totalSum / lens
    print("Стандартне відхилення = ", str(round(math.sqrt(result))))
    print("Середнє відхилення = ", str(round(Result)))

    sus.write("\nСтандартне відхилення = " + str(round(math.sqrt(result))))
    sus.write("\nСереднє відхилення = " + str(round(Result)))
#==================================================
def task3():
    sum = 0
    result = []
    for i in data:
        sum += i
    a = np.array([[100, 1, ], [(sum / lens), 1, ]])
    #|100 = 100*a + b
    #|95 = 74.2*a + b
    x = solve(a, np.array([100, 95]))
    for i in range(lens):
        result.append(round(x[0] * data[i] + x[1]))
    print("Старі оцінки: " + str(data))
    sus.write("\nСтарі оцінки: " + str(data))



    print("\nНові оцінки: " + str(result))
    sus.write("\nНові оцінки: " + str(result))
#==================================================
def task4():
    print("Діаграма стовбур-листя")
    print("-----------------------")

    sus.write("\nДіаграма стовбур-листя")
    sus.write("\n-----------------------")

    i = min(data)

    while i <= max(data):
        mas = []
        for j in range(lens):
            if i < data[j] < i + 10:
                mas.append(data[j] % 10)
            elif data[j] == i:
                mas.append(0)
        if len(mas) != 0:
            print(str(i / 10) + " \t| " + str(mas))
            sus.write("\n" + str(i / 10) + " \t| " + str(mas))
        i += 10
    print("Ключ = " + str(data[0]))
    sus.write("\nКлюч = " + str(data[0]))
# ==================================================
def task5():
    plt.boxplot(data)
    plt.grid()
    plt.show()
print("Task 1:")

Q1 = task1(1 / 4)
Q3 = task1(3 / 4)
P90 = task1(0.9)

print("Q1 = ", Q1)
print("\nQ3 = ", Q3)
print("\nP90 = ", P90)

sus.write("\nQ1 = ")
sus.write(str(Q1))
sus.write("\nQ3 = ")
sus.write(str(Q3))
sus.write("\nP90 = ")
sus.write(str(P90))
print("Task 2:")
task2()
print("Task 3 :")
task3()
print("Task 4:")
task4()
task5()
sus.close()