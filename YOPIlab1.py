import math
import matplotlib.pyplot as plt
import sys

#sys.stdout = open("result.txt", "w")
def SetData(FileName, data):


    file = open(FileName, 'r')
    for line in file:
        data.append(int(line.strip()))
data = []
SetData('input_10.txt', data)

# ____________________________________

# Ex. 1

def TableBuild(data):
    print("Film\t\tFreq.\t  Cumulative freq.")
    cum_freq = 0
    counter = 0
    for item in data:
        counter += item
    for item in sorted(set(data)):
        freq = data.count(item)
        cum_freq += freq
        print("|", item, "\t | \t", freq, "\t | \t", cum_freq, "|")
    print("Total:", counter)


TableBuild(data)

print("Most views:", max(data))

# ____________________________________

# Ex. 2

def Mediana(data_argument):
    if len(data_argument) % 2 == 0:
        median = (data_argument[int(len(data_argument) / 2)] + data_argument[int(len(data_argument) / 2) - 1]) / 2
    else:
        median = data_argument[int(len(data_argument) / 2) + 1]
    return median
print("Mediana =", Mediana(sorted(data)))

def Moda(data_argument):
    Moda = 0
    ModaN = 0
    for i in data_argument:
        if ModaN < data_argument.count(i):
            Moda = data_argument[i]
            ModaN = data_argument.count(i)
    return Moda
print("Moda =", Moda(data))
#print('Moda-',max(set(data), key=data.count))

# ____________________________________

# Ex. 3

Dispersion = 0
for i in data:
    Dispersion += ((i - (sum(data) / len(data))) ** 2) / (len(data) - 1)
print("Dispersion =", round(Dispersion, 3))

print("Average square deviation =", round(math.sqrt(Dispersion), 3))

# ____________________________________

# Ex. 4

plt.hist(sorted(data), facecolor='purple', align='mid', alpha=0.5)
plt.xlabel("Film")
plt.ylabel("Frequency")
plt.show()

# ____________________________________

 #sys.stdout.close()