import csv
import math
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

squaredList = []
for number in data:
    a = int(number) - mean(data)
    a1 = a**2
    squaredList.append(a1)
sum = 0
for i in squaredList:
    sum = sum + i
result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)