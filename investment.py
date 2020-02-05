#! /usr/bin/env python3

amount = float(input())
inrate = float(input())
period = int(input())

value = 0
year = 1

while year <= period:
    value = amount + (amount*inrate)
    print("year {} Rs, {:.2f}".format(year, value))
    amount = value
    year = year+1
