

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from utils.primes import is_prime
from itertools import permutations

ans = 0
p = ['1','2','3']
for i in range(4,10):
	p += [str(i)]
	for s in permutations(p):
		v = int(''.join(s))
		if is_prime(v):
			# print(v)
			ans = max(ans, v)
print(ans)
