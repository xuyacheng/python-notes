#! /usr/bin/env python3

while True:
    n = int(input())
    if n < 0:
        continue
    elif n == 0:
        break
    else:
        print(n**2)

