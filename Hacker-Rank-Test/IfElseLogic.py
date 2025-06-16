import math
import os
import random
import re
import sys
import time

n = int(input().strip())

# 1. Cek jika n adalah ganjil
if n % 2 != 0:
    print("Weird")
# 2. Jika tidak (berarti n adalah genap), baru periksa kondisi selanjutnya
else:
    # 2a. Cek jika n genap DAN berada di rentang 2-5 (inklusif)
    if n >= 2 and n <= 5:
        print("Not Weird")
    # 2b. Cek jika n genap DAN berada di rentang 6-20 (inklusif)
    elif n >= 6 and n <= 20:
        print("Weird")
    # 2c. Cek jika n genap DAN lebih dari 20
    elif n > 20:
        print("Not Weird")