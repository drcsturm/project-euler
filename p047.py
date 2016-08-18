

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2**2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

from utils.primes import is_prime
from utils.common import prime_factors

num = 2 * 3 * 5 * 7
while True:
	if is_prime(num+3):
		num += 4
		continue
	if is_prime(num+2):
		num += 3
		continue
	if is_prime(num+1):
		num += 2
		continue
	n1 = len(set(prime_factors(num))) == 4
	n2 = len(set(prime_factors(num+1))) == 4
	n3 = len(set(prime_factors(num+2))) == 4
	n4 = len(set(prime_factors(num+3))) == 4
	if n1 and n2 and n3 and n4:
		print(num)
		break
	num += 1
