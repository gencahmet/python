import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n %2 == 1:
    print("Weird")
if n%2 ==0:
    if n in range(2,5) or n>20:
        print("Not Weird")
    
    else:
        print("Weird") 
  