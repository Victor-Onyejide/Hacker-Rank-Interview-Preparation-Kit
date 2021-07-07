#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sum_up = {}
    for i in range(0,n-1):
        count = 1
        # if sum_up:
        if check_keys(sum_up.keys(), ar[i]) == True:
                continue
                
        for j in range(i + 1,  n):
            if ar[i] == ar[j]:
                count += 1
        pairs = math.floor(count / 2)
        sum_up[ar[i]]= pairs
    
    #Total
    total_sum = sum(sum_up.values())
    return total_sum
                
def check_keys(sum_up_keys, l_i):
    for k in sum_up_keys:
        if k == l_i:
            return True
    return False
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
