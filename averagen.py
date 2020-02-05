#! /usr/bin/env python3

N = 10
sum = 0
count = 0

while count < N:
    number = float(input())
    sum += number
    count += 1
average = sum / N

print("N={}, sum={}".format(N, sum))
print("average={:.2f}".format(average))
