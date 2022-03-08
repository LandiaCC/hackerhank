#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    def r_pm(s):
        padrao = re.compile("PM")
        return bool(padrao.search(s))
    
    def get_hour_min_sec(s):
        padrao = re.compile("\D+")
        lsh = padrao.split(s)
        return (lsh[0], lsh[1], lsh[2])
    
    def convert_hora_am(hora):
        hora_int = int(hora)
        r_hora_12 = hora_int == 12
        hora_mi = hora_int
        if r_hora_12:
            hora_mi = abs(hora_int - 12)

        r_eq_24 = hora_mi == 24
        r_menor_10 = hora_mi < 10
        if r_eq_24:
            return "00"
        if r_menor_10:
            return f"0{hora_mi}"
        else:
            return f"0{hora_mi}"

    def convert_hora_pm(hora):
        hora_int = int(hora)
        hora_mi = hora_int
        r_hora_dif_12 = hora_int != 12
        if r_hora_dif_12:
            hora_mi = hora_int + 12
             
        r_eq_24 = hora_mi == 00
        r_menor_10 = hora_mi < 10
        if r_eq_24:
            return "00"
        if r_menor_10:
            return f"0{abs(hora_mi)}"
        else:
            return f'{abs(hora_mi)}'
    
    hora, min, seg = get_hour_min_sec(s)

    if r_pm(s):
        return f'{convert_hora_pm(hora)}:{min}:{seg}'
    else:
        return f'{convert_hora_am(hora)}:{min}:{seg}'
        
        
    
        
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print('06:40:03AM',timeConversion('06:40:03AM'))
    print('12:45:54PM', timeConversion('12:45:54PM'))
    print('07:05:45PM', timeConversion('07:05:45PM'))

    # fptr.write(result + '\n')

    # fptr.close()
