#!/bin/python3

import math
import os
import random
import re
import sys

def calculateHourGlass(arr , i , j):
    a = arr[i][j]
    b = arr[i][j+1]
    c = arr[i][j+2]
    d = arr[i+1][j+1]
    x = arr[i+2][j]
    y = arr[i+2][j+1]
    z = arr[i+2][j+2] 

    sum = (a+b+c+d+x+y+z)

    return sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
 
    res = []

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum = calculateHourGlass( arr , i , j)
            res.append(sum)
    print(max(res))        
