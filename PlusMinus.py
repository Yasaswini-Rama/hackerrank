import math
import os
import random
import re
import sys
def plusMinus(arr):
    # Write your code here
    p = n = z = 0
    for i in arr:
        if i > 0 :
            p += 1
        elif i < 0 :
            n += 1
        else :
            z += 1
    print(p/len(arr),"\n", n / len(arr),"\n",z / len(arr))   
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
