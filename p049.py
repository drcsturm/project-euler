

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?
from itertools import permutations
from utils.primes import primesfrom2to, is_prime

found = False
for p in primesfrom2to(10000):
	if p < 1000:continue
	perms = tuple(permutations(list(str(p))))
	if ('1','4','8','7') in perms:continue
	for s1 in perms:
		n1 = int(''.join(s1))
		if n1 < 1000:continue
		if not is_prime(n1):continue
		for s2 in perms:
			if s2 == s1:continue
			n2 = int(''.join(s2))
			if n2 < 1000:continue
			if not is_prime(n2):continue
			for s3 in perms:
				if s3 == s1 or s3 == s2:continue
				n3 = int(''.join(s3))
				if n3 < 1000:continue
				if not is_prime(n3):continue
				if abs(n1 - n2) == abs(n2 - n3):
					found = True
				if found:break
			if found:break
		if found:break
	if found:break
if found:
	print(''.join([str(i) for i in sorted([n1,n2,n3])]))
