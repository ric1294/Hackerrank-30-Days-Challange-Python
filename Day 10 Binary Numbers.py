#!/bin/python3

import math
import os
import random
import re
import sys


def maxConsecutiveOnes(x): 
  
    # Initialize result 
    count = 0
   
    # Count the number of iterations to 
    # reach x = 0. 
    while (x!=0): 
      
        # This operation reduces length 
        # of every sequence of 1s by one. 
        x = (x & (x << 1)) 
   
        count=count+1
      
    return count 
# def DecimalToBinary(num): 
      
   

if __name__ == '__main__':
    n = int(input())

    print(maxConsecutiveOnes(n))
    #DecimalToBinary(n)

     
