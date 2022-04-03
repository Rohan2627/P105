import pandas as pd
import statistics
import math
import csv


with open("project105.csv") as f:
    data = csv.reader(f)
    df = list(data)

x = df[0]

# print(x)

mean = statistics.mean(x)

squaredList = []

for i in x:
    a = int(i)- mean
    a = a**2 

    squaredList.append(a)


sum = 0

for i in squaredList:
    sum = sum + int(i)

total = len(x)
stdev = math.sqrt( sum/(total-1) )

print(stdev)