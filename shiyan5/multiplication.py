#! /usr/bin/env python3

i = 1

print("-"*50)
while i <= 10:
    j = 1
    while j <= 10:
        print("{:5d}".format(i*j), end='')
        j += 1
    print()
    i += 1

print("-"*50)
