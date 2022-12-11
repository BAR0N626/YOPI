import math
import matplotlib.pyplot as plt
import sympy as sp
import sys

sus = open("result.txt", "w+")
averagex, averagey = 0.0, 0.0
def connect_txt(nameoffile):
    inputdata = []
    input = open("input_103.txt")
    input.seek(1)
    for line in input:
        inputdata.append(input.read(3))
        input.read(1)
        inputdata.append(input.read(2))
    for i in range(int(len(inputdata))):
        inputdata[i] = inputdata[i].replace(',', '.')
    data = [[0 for i in range(2)] for j in range(int(len(inputdata) / 2))]
    index0 = 0
    index1 = 0
    for i in range(int(len(inputdata))):
        if i % 2 == 0:
            data[index0][0] = float(inputdata[i])
            index0 +=1
        elif i % 2 != 0:
            data[index1][1] = int(inputdata[i])
            index1 += 1
    return data

def dataX(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][0])
    return inputdatadata

def dataY(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][1])
    return inputdatadata


def trend(data):
    if max(data) == data[len(data)-1]:
        print("Тренд даних позитивний") # Якщо останній єлемент з вибірки дорівнює максимальному, то тренд позитивний
        sus.write("\nТренд даних позитивний")
    elif min(data) == data[len(data)-1]:
        print("Тренд даних негативний")
        sus.write("\nТренд даних негативний")
    else:
        print("Данні не мають тренду")
        sus.write("\nДанні не мають тренду")


def covariance(x, y):
    global averagex, averagey
    covarience = 0.0
    for i in range(len(x)):
        averagex += x[i]
        averagey += y[i]
    averagex = averagex / len(x)
    averagey = averagey / len(y)
    for i in range(len(x)):
        covarience += (x[i] - averagex) * (y[i] - averagey)
    covarience = covarience / (len(x)-1)
    print("Коваріацію: ", covarience)
    sus.write("Коваріацію: " + str(covarience))


def correlation(x, y):
    global averagex, averagey
    corcoef, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
    for i in range(len(x)):
        sum1 += (x[i] - averagex) * (y[i] - averagey)
        sum2 += (x[i] - averagex) * (x[i] - averagex)
        sum3 += (y[i] - averagey) * (y[i] - averagey)
    sum2 = sum2 * sum3
    corcoef = sum1/math.sqrt(sum2)
    print("Коефіцієнт кореляції:", corcoef)
    sus.write("\nКоефіцієнт кореляції:" + str(corcoef))


def lineofregression(X, Y):
    global averagex, averagey
    byx, sumx, sumy, sumxy, sumx2, sumy2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(len(X)):
        sumx += X[i]
        sumy += Y[i]
        sumxy += X[i] * Y[i]
        sumx2 += X[i] * X[i]
        sumy2 += Y[i] * Y[i]
    byx = (len(X) * sumxy - (sumx * sumy)) / (len(X) * sumx2 - sumx2)
    x, y = sp.symbols("x,y")
    line = sp.Eq(y-averagey, byx*(x-averagex))
    linex = sp.solve(line, y)
    liney = sp.solve(line, x)
    strlinex = str(linex)
    strliney = str(liney)
    strlinex = strlinex.replace("[", "")
    strlinex = strlinex.replace("]", "")
    strliney = strliney.replace("[", "")
    strliney = strliney.replace("]", "")
    print("Лінія регресії y від x. ")
    print("x = " + strliney)
    print("y = " + strlinex, "\t(у від х)")
    sus.write("Лінія регресії y від x.\n")
    sus.write("x = " + strliney)
    sus.write("\ny = " + strlinex + "\t(у від х )")



input = connect_txt("input_103.txt")
data = sorted(input)
infoX = dataX(data)
infoY = dataY(data)
print("Відсортовані данні: ", data)
sus.write("Відсортовані данні: " + str(data))
print("\n")
sus.write("\n\n")
trend(data)
print("\n")
sus.write("\n\n")
covariance(infoX, infoY)
correlation(infoX, infoY)
print("\n")
sus.write("\n\n")
lineofregression(infoX, infoY)
plt.scatter(infoX, infoY)
plt.show()