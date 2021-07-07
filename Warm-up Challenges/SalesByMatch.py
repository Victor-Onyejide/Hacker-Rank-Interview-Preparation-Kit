#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    colorsandpairs = {}
    for i in range(0,n-1):
        count = 1
        if check_keys(colorsandpairs.keys(), ar[i]) == True:
            continue
        for j in range(i+1,n):
            if ar[i] == ar[j]:
                count +=1
        pairs = math.floor(count/2)
        
        colorsandpairs[ar[i]] = pairs
        
    total_sum = sum(colorsandpairs.values())
    return total_sum
    
def check_keys(keys, l_i):
    for k in keys:
        if k == l_i:
            return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
