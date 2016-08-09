# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math
from utils.primes import primesfrom2to
test_num = 600851475143
# test_num = 10000

num = int(math.sqrt(test_num))
plist = primesfrom2to(num)
for i in reversed(plist):
    if test_num % i == 0:
        print(i)
        break
