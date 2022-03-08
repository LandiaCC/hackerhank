#!/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    def soma(array):
        return reduce(lambda x,y: x+y, array)
    
    arra_pos = sorted(arr)
        
    ar_min = soma(arra_pos[0:4])
    ar_max = soma(arra_pos[1:5])

    print(f'{ar_min} {ar_max}')
    # ar_max = 
    
    
    print()

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
