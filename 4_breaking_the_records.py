#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    
    ult_scor_max = scores[0]
    ult_scor_min = scores[0]
    int_scor_max = 0
    int_scor_min = 0
    
    for scor_item in scores[1:]:
        r_maior = scor_item > ult_scor_max
        r_menor = scor_item < ult_scor_min
        
        if r_maior:
            ult_scor_max = scor_item
            int_scor_max += 1
        
        if r_menor:
            ult_scor_min = scor_item
            int_scor_min += 1
        
        
        
    return [int_scor_max, int_scor_min]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
