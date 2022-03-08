#!/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    qnt_array = len(arr)
    p_pos = len(list(filter(lambda x: x>0, arr))) / qnt_array
    p_neg = len(list(filter(lambda x: x<0, arr))) / qnt_array
    p_zero = len(list(filter(lambda x: x==0, arr))) / qnt_array
    
    print(p_pos)
    print(p_neg)
    print(p_zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
