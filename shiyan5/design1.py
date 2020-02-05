#! /usr/bin/env python3

N = 5

for i in range(0, N):
    print("*"*(N-i))

print()

for i in range(1, N+1):
    print("*"*i)

print()

for i in range(0, N):
    print(" "*i, end='')
    print("*"*(N-i))
